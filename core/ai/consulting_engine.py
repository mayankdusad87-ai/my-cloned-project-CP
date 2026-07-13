"""
=========================================================
ChannelIQ AI

Consulting Engine

Main orchestration layer for AI Consulting.

Flow

AnalysisResult
      ↓
Context Builder
      ↓
Findings Engine
      ↓
Prompt Builder
      ↓
AI Provider
      ↓
Executive Report

=========================================================
"""

from __future__ import annotations

import json

from core.analysis_result import AnalysisResult
from core.ai.context_builder import ContextBuilder
from core.ai.findings_engine import FindingsEngine
from core.ai.provider import AIProvider
from core.ai.validator import AIResponseValidator

from core.ai.prompts import (
    SYSTEM_PROMPT,
    EXECUTIVE_SUMMARY_PROMPT,
    OUTPUT_FORMAT,
)


class ConsultingEngine:
    """
    Main AI Orchestrator.

    This class never talks directly to OpenAI.

    It only talks to AIProvider.
    """

    def __init__(
        self,
        provider: AIProvider,
    ):

        self.provider = provider

        self.context_builder = ContextBuilder()

        self.findings_engine = FindingsEngine()

        self.validator = AIResponseValidator()

    # =====================================================
    # PUBLIC
    # =====================================================

    def generate(
        self,
        result: AnalysisResult,
    ) -> dict:

        # --------------------------------------------
        # Build Context
        # --------------------------------------------

        context = self.context_builder.build(
            result
        )

        # --------------------------------------------
        # Generate Findings
        # --------------------------------------------

        findings = self.findings_engine.analyse(
            context
        )

        # --------------------------------------------
        # Merge
        # --------------------------------------------

        payload = {

            "context": context,

            "findings": findings,

        }

        # --------------------------------------------
        # Prompt
        # --------------------------------------------

        user_prompt = self.build_prompt(
            payload
        )

        # --------------------------------------------
        # AI
        # --------------------------------------------

        response = self.provider.generate(

            system_prompt=SYSTEM_PROMPT,

            user_prompt=user_prompt,

        )
        validated_response = self.validator.validate(response)
        
        return validated_response 

    # =====================================================
    # PROMPT
    # =====================================================

    def build_prompt(
        self,
        payload: dict,
    ) -> str:

        prompt = f"""

{EXECUTIVE_SUMMARY_PROMPT}

========================================================

BUSINESS FACTS

========================================================

{json.dumps(payload, indent=4, default=str)}

========================================================

IMPORTANT

========================================================

Use ONLY supplied business facts.

Never invent KPIs.

Never invent numbers.

Never contradict supplied metrics.

{OUTPUT_FORMAT}

"""

        return prompt
