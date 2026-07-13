"""
=========================================================
ChannelIQ AI

Analysis Result Model

This class is the single source of truth
for an analysed Excel file.
=========================================================
"""

from dataclasses import dataclass, field
from typing import Dict, List
import pandas as pd


@dataclass
class KPI:

    name: str

    value: float | int | str

    change: float = 0

    status: str = "neutral"


@dataclass
class PartnerScore:

    partner_name: str

    bookings: int

    conversion: float

    score: float

    category: str

    risk: str

    opportunity: float


@dataclass
class AnalysisResult:

    # --------------------------------------------------
    # Basic Information
    # --------------------------------------------------

    analysis_id: str = ""

    company_name: str = ""

    project_name: str = ""

    month: str = ""

    year: int = 0

    ai_report: Dict = field(default_factory=dict)

    # --------------------------------------------------
    # Raw Data
    # --------------------------------------------------

    dataframe: pd.DataFrame | None = None

    # --------------------------------------------------
    # Dashboard KPIs
    # --------------------------------------------------

    health_score: float = 0

    total_bookings: int = 0

    conversion: float = 0

    revenue_opportunity: float = 0

    growth_rate: float = 0

    high_risk_partners: int = 0

    # --------------------------------------------------
    # Business Intelligence
    # --------------------------------------------------

    kpis: List[KPI] = field(default_factory=list)

    partner_scores: List[PartnerScore] = field(default_factory=list)

    trends: Dict = field(default_factory=dict)

    risks: Dict = field(default_factory=dict)

    opportunities: Dict = field(default_factory=dict)

    funnel: Dict = field(default_factory=dict)

    # --------------------------------------------------
    # AI
    # --------------------------------------------------

    executive_summary: str = ""

    recommendations: List[str] = field(default_factory=list)

    predictions: List[str] = field(default_factory=list)

    # --------------------------------------------------
    # Export
    # --------------------------------------------------

    charts: Dict = field(default_factory=dict)

    metadata: Dict = field(default_factory=dict)

    # --------------------------------------------------

    def has_data(self):

        return self.dataframe is not None

    # --------------------------------------------------

    def dashboard_metrics(self):

        return {

            "Health":

                self.health_score,

            "Bookings":

                self.total_bookings,

            "Conversion":

                self.conversion,

            "Revenue":

                self.revenue_opportunity,

            "Growth":

                self.growth_rate

        }

    # --------------------------------------------------

    def add_recommendation(self, text):

        self.recommendations.append(text)

    # --------------------------------------------------

    def add_prediction(self, text):

        self.predictions.append(text)
