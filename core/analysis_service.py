"""
=========================================================
ChannelIQ AI

Analysis Service

This class orchestrates the complete analysis process.

Flow

Excel
    ↓
Validation
    ↓
Data Processing
    ↓
Scoring
    ↓
Trend Analysis
    ↓
Risk Analysis
    ↓
Opportunity Analysis
    ↓
AI
    ↓
AnalysisResult
=========================================================
"""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from core.analysis_result import AnalysisResult
from core.excel_reader import ExcelReader
from utils.validators import TemplateValidator


class AnalysisService:
    """
    Main business orchestration class.

    This class coordinates the complete analysis workflow.
    It does not perform business calculations itself.
    """

    def __init__(self) -> None:

        self.reader = ExcelReader()
        self.validator = TemplateValidator()

    # =======================================================
    # PUBLIC
    # =======================================================

    def analyse(
        self,
        excel_file,
        company_name: str,
        project_name: str,
        month: str,
        year: int,
    ) -> AnalysisResult:

        # Create a fresh result object for every analysis
        result = AnalysisResult()

        # Initialise metadata
        self._initialise_metadata(
            result=result,
            company=company_name,
            project=project_name,
            month=month,
            year=year,
        )

        # Read Excel
        df = self.reader.read(excel_file)

        # Validate template
        self.validator.validate(df)

        # Store dataframe
        result.dataframe = df

        # Temporary metrics
        self._calculate_basic_metrics(result)

        return result

    # =======================================================
    # PRIVATE
    # =======================================================

    def _initialise_metadata(
        self,
        result: AnalysisResult,
        company: str,
        project: str,
        month: str,
        year: int,
    ) -> None:

        result.analysis_id = (
            datetime.now().strftime("%Y%m%d")
            + "-"
            + uuid4().hex[:8].upper()
        )

        result.company_name = company
        result.project_name = project
        result.month = month
        result.year = year

    # =======================================================

    def _calculate_basic_metrics(
        self,
        result: AnalysisResult,
    ) -> None:
        """
        Temporary placeholder KPIs.

        In the next sprint this method will be replaced by:

            DataProcessor
            ScoringEngine
            TrendEngine
            RiskEngine
            OpportunityEngine
        """

        df = result.dataframe

        result.total_bookings = 0
        result.conversion = 0
        result.health_score = 0
        result.revenue_opportunity = 0
        result.growth_rate = 0
        result.high_risk_partners = 0

        result.metadata = {
            "rows": len(df),
            "columns": len(df.columns),
            "generated_at": datetime.now().isoformat(),
        }
