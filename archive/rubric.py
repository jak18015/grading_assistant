# TOTAL_POSSIBLE_GRADEPOINTS
GEL_DESIG = 1
ELECTROPHORESIS_TIMES = 2
LOADED_LANES = 3
TABLE_12_1 = 36
STANDARD_CURVE = 18

DESCRIPTIVE_FIGURE = 20

DISCUSSION_25 = 4
DISCUSSION_250 = 4
DISCUSSION_400 = 4
CONCLUSIONS = 4
CLINICAL_SIGNIF = 4
OTHER = 0

POINTS_POSSIBLE: tuple = (
    GEL_DESIG,
    ELECTROPHORESIS_TIMES,
    LOADED_LANES,
    TABLE_12_1,
    STANDARD_CURVE,
    DESCRIPTIVE_FIGURE,
    DISCUSSION_25,
    DISCUSSION_250,
    DISCUSSION_400,
    CONCLUSIONS,
    CLINICAL_SIGNIF,
    OTHER,
)

criteria: list = [
    "Lab notebook: designate which gel was loaded",
    "Lab notebook: note the start/end time for gel electrophoresis",
    "Lab notebook: note the loaded lanes",
    "Lab notebook: Table 12.1",
    "Lab notebook: Standard curve on semi-log paper",
    "Figure: Descriptive figure for SDS-PAGE gel",
    "Discussion:  25mM imidazole:\n    Discuss molecular weight range of proteins eluted\n    Discuss molecular weight of most prominent band\n    Discuss how this was determined",
    "Discussion: 250mM imidazole:\n    Discuss molecular weight range of proteins eluted\n    Discuss molecular weight of most prominent band\n    Discuss how this was determined",
    "Discussion: 400mM imidazole:\n    Discuss molecular weight range of proteins eluted\n    Discuss molecular weight of most prominent band\n    Discuss how this was determined",
    "Conclusions and possible sources of error:",
    "Clinical significance:",
    "Other:",
]
