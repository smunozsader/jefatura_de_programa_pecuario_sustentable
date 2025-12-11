# AI Agent Instructions: Macroproyecto Renacimiento Ganadero Maya

## Project Overview
This workspace contains documentation for a comprehensive agricultural strategic program in Yucatán, Mexico (2026-2030). The "Renacimiento Ganadero Maya" macroproject is a **$1,087.9 million MXN** strategic program prepared by **MVZ Sergio Muñoz de Alba Medrano, Independent Consultant**. The project focuses on sustainable livestock transformation, cattle repopulation with intensive silvopastoral systems, animal health certification, and international export capabilities. The project integrates six interdependent components designed to position Yucatán as Mexico's leader in climate-smart livestock production.

**AUTHORSHIP NOTE**: Document prepared as independent consultant work coto be presented to SEDER Yucatán, not as federal SADER employee. No institucional branding as of yet, as it is independent consultancy. However, the institutional structure is as follows: 
SADER, SENASICA, and OREF retain their institutional coordination and funding facilitation roles for the paripassu federal-state funding scheme, while the primary institutional authority commissioning the work is the Gobierno del Estado de Yucatán through SEDER with Prof. Edgardo Medina as Secretary.
Please ensure all documents reflect this institutional structure appropriately. Remove logos on title pages that imply federal authorship; also remove logos on all other pages (remove the logos from headers). ### ** 

**INSTITUTIONAL STRUCTURE**:
- **Primary Leadership**: This is an independant proposal, to be presented to the Yucatán State Government, specically to the head of Secretaria de Desarollo Rural (SEDER) by its author.
- **Federal Coordination Role**: SADER and OREF maintaining their essential coordination and funding facilitation role for the paripassu federal-state funding scheme
- **Independent Authorship**: MVZ Sergio Muñoz de Alba Medrano, Independent Consultant, commissioned by SEDER Yucatán

This structure properly acknowledges that while the consultant is now independent, the federal agencies still have their institutional coordination and funding roles, which is essential for a project requesting federal funds through the concurrence scheme. The emphasis is on state government leadership while maintaining the necessary federal partnership for implementation. There should be no branding but the institutional governance correctly positions the Yucatán State Government and SEDER as the primary institutional authorities proposed to lead the work, with federal agencies in their appropriate coordination and funding facilitation role.

## Core Architecture & Components

### Six Integrated Strategic Components ($1,035.1 million MXN productive investments)
1. **Intensive Silvopastoral Systems (SSPi)** - $500.1M hybrid financing ($333.4M subsidio + $166.7M crédito, 6,000 ha conversion, 120 UPP, $55,573/ha technical package with Leucaena leucocephala at 40,000-53,000 plants/ha, 6.0 kg/ha seeding rate)
2. **Cattle Repopulation Program** - $150.1M (12,000 F1 heifers, 1,075 UPP, strategic livestock replacement)
3. **Genetic Improvement Center (Tizimín)** - $150.0M (Center refoundation, ISO/IEC 17025:2017 certification, OIE accreditation, 120,000 semen doses/year)
4. **Tropical Dairy Development** - $89.5M (75 technified modules, +40% milk production increase, specialized silvopastoral systems)
5. **Sustainable Maya Meliponiculture** - $42.5M (500 producers, 350 women beneficiaries, native bee conservation with Melipona beecheii)
6. **Digital Sanitary Platform (CESO)** - $51.5M (T-MEC compliance, APHIS-USDA protocols, digital traceability)

**NOTE**: Component 5 "Sterile Fly Plant" appears as separate strategic component in `MOSCA ESTERIL/` directory with independent $300M budget. Current main document reflects 6 components optimized structure.

### Updated Investment Breakdown (Corrected Values with Hybrid Financing)
- **Productive Investments**: $1,035.1M (95.1%)
- **Operational Expenses**: $52.8M (4.9% - 5-person technical team: 1 Program Manager + 4 staff via SEDER Yucatán)
- **Total Project Value**: $1,087.9M (includes all 6 strategic components with hybrid financing)
- **Hybrid Financing Schema**: $921.2M Tripartite Subsidy (60% Federal + 30% State + 10% Producers) + $166.7M Productive Credit (50% of SSPi component)
- **SSPi Credit Model**: 50% credit financing ($27,787/ha) with 4.0:1 payment capacity ratio based on beef calf weaning system (+1,167% productivity increase)

**CRITICAL NOTE**: The main LaTeX document now reflects all 6 strategic components with corrected values and hybrid financing model. The $1,087.9M total includes: SSPi realistic costing ($333.4M using recommended scenario $55,573/ha from technical calculation memory), all 6 distinct components, operational costs, and integrated credit financing model. Based on scientifically validated calculations with beef calf weaning economic model showing 4.0:1 payment capacity ratio for 50% credit financing of SSPi component.

### Key File Structure
- `Proyecto Estrategico/`: Core strategic documents
  - `MACROPROYECTO_INTEGRADO_GANTT_2026-2030.tex`: Main executive document (LaTeX, 60+ pages, APA citations, calculation memories)
  - `BASE_TECNICA_INTEGRAL_RENACIMIENTO_GANADERO_MAYA.tex`: Technical foundation document
  - `RESUMEN_EJECUTIVO_*.tex`: Multiple executive summaries (telegraphic pitch, epic storytelling, standard)
  - `MEMORIA_CALCULO_PAQUETE_TECNOLOGICO_SSPi.tex`: SSPi technical calculation memories
  - `ESTRUCTURA_PRESUPUESTARIA_CORRECTA.md`: Consolidated budget structure
  - `Analisis Pareto Ganadero Yucatan.tex`: Territorial focusing analysis (11 municipalities = 80.3% concentration)
- `ANALISIS Y SCRIPTS/`: Python data analysis tools
  - `budget_analysis.py`: Budget coherence verification with SIAP data integration
  - `extraccion_detallada_sspi.py`: PDF text extraction for SSPi research analysis
  - `analisis_sspi_pdfs.py`: Scientific literature mining tool
- `Descripcion de Puesto. Jefe de Programa/`: Program management documentation
  - `DescripcionPuesto_JefePrograma_LATEX.tex`: Technical coordinator profile (8-person team)
- `DOCS REFERENCIA/`: Supporting documentation, SIAP data, scientific articles
  - `2025. padron ganadero nacional yucatan detallado por municipios.gsheet`: Official livestock census
  - `2025. siap. datos pecuarios/`: Official livestock inventory data
  - `articulos lecheros/`: Scientific references for tropical dairy systems
  - `guia metodologica para la incorporacion de escuelas de campo de sistemas silvopastoriles (colombia).pdf`: SSPi implementation methodology
- `MOSCA ESTERIL/`: Separate strategic component for screwworm eradication ($300M independent project)
- `Centro de Mejoramento Genetico/`: Genetic improvement center documentation
- `SANIDADES/`: Animal health certification protocols

## Document Conventions

### LaTeX Document Standards
- **CRITICAL**: Always compile LaTeX documents TWICE using `pdflatex` to properly populate table of contents and cross-references
- **Terminal Command**: `cd "Proyecto Estrategico" && pdflatex MACROPROYECTO_INTEGRADO_GANTT_2026-2030.tex && pdflatex MACROPROYECTO_INTEGRADO_GANTT_2026-2030.tex`
- **Document Class**: Use `\documentclass[12pt,letterpaper,titlepage]{article}` with UTF-8 encoding and Spanish/Mexico babel
- **Essential Packages**: geometry, graphicx, fancyhdr, booktabs, xcolor, colortbl, pgfgantt, tabularx, float, multirow, lastpage
- **Page Layout**: Geometry with left=3cm, right=2.5cm, top=3cm, bottom=3cm margins, headheight=20pt
- **Colors**: Define SADER palette: sadergreen RGB(0,102,51), sadergris RGB(80,80,80), sadergold RGB(204,153,0), saderblue RGB(0,51,102)
- **Headers/Footers**: ALL documents MUST use fancy headers with document title centered and fancy footers with "Página X de Y" format using LastPage reference. Format: `\fancyhead[C]{\textcolor{sadergris}{\footnotesize DOCUMENT TITLE}}` and `\fancyfoot[C]{\textcolor{sadergris}{\small Página \thepage\ de \pageref{LastPage}}}`
- **Title Pages**: Include institutional hierarchy, authorship, investment totals, component summary
- **Tables**: Extensive use with rowcolor alternation (sadergreen!20, sadergold!30), booktabs formatting
- **Gantt Charts**: Use pgfgantt package for timeline visualization with component dependencies
- **Professional Structure**: Titlepage → table of contents → sections with decimal numbering (1., 1.1., 1.1.1.)

### Scientific Citation Requirements
- **APA Citation System**: All quantitative claims must include numbered superscript citations (\textsuperscript{1,2,3})
- **Calculation Memories**: Include detailed technical annexes (Anexo III, IV, V) with transparent calculation methodologies
- **Bibliography**: Numbered references in APA format with full scientific traceability
- **Mathematical Formulas**: Use proper LaTeX math formatting (avoid \$ inside formulas, use CO$_2$ not CO\$_2\$)

### Enhanced Writing Standards (Mexican Spanish)
- **Formal Technical Language**: Use Mexican Spanish formal conventions reflecting SADER/BID best practices with complex but clear syntax, technical vocabulary ("reconversión territorial", "carga animal", "trazabilidad sanitaria"). Respect Mexican grammatical rules: correct prepositions ("en el marco de" not "dentro de"), proper articles ("el hato ganadero" vs "un hato"), gender/number concordance
- **Objective Tone**: Maintain persuasive, prospective tone with quantifiable benefits (ROI, CO₂ capture) without exaggerations. Avoid colloquial language; use phrases like "los datos oficiales SIAP confirman" to support claims
- **Terminological Consistency**: Define acronyms on first mention (SINIIGA as Sistema Nacional de Identificación Individual de Ganado), maintain uniform usage throughout. Handle terms like "SSPi" and "GBG" consistently across documents
- **Social Inclusion**: Address impacts on Maya communities, gender equity (women producers participation), and indigenous peoples aligned with Ley de Desarrollo Rural Sustentable
- **Evidence-Based Content**: Ground all claims in SIAP, SINIIGA, SINIDA, CNOG, T-MEC, INIFAP, FAO data with bibliographic references
- **Document Structure**: Follow modular organization: cover, detailed index, executive summary (max 2 pages), background/justification, detailed components, quarterly Gantt timeline, consolidated budget, impact indicators, conclusions, bibliography, annexes
- **Hierarchical Organization**: Use decimal numbering (1., 1.1., 1.1.1.) with introduction, body, and transitional closures highlighting component interconnections
- **Mandatory Visual Elements**: Tables, diagrams, graphics, Gantt charts with progress bars and dependencies (e.g., GBG eradication before TBC certification)
- **Cross-References**: Employ "véase Anexo V" style references to avoid repetitions
- **Visual Elements**: Include mandatory tables, diagrams, graphics, Gantt charts with progress bars and dependencies
- **Length Control**: 50-100 main pages + annexes, avoid repetitions, use cross-references

### Financial Reporting Standards
- All monetary values in Mexican Pesos (MXN) with MDP (millones de pesos) abbreviation
- 5-year projection tables (2026-2030) for all financial components
- Detailed budgets with tables broken down by component, year, and source (federal via FOFAY, state, private)
- Include TIR, VAN analysis and amortization by environmental services
- Concurrency schema: 60% federal ($465.9M) - 30% state ($232.95M) - 10% producers ($77.65M)
- FOFAY (Fideicomiso Fondo de Fomento Agropecuario Yucatán) as operational financial mechanism
- PEC (Programa Especial Concurrente) budget requests as primary federal funding mechanism
- Sustainability metrics: CO₂ capture, nitrogen fixation, employment, small producer inclusion
- SMART verifiable indicators (6,000 ha converted, 12,000 F1 heifers, 75% productivity increase)

### Institutional Terminology
- **SEDER**: Secretaría de Desarrollo Rural del Gobierno del Estado de Yucatán (primary institutional authority for this project)
- **SADER**: Secretaría de Agricultura y Desarrollo Rural (federal agriculture ministry - coordination role)
- **SENASICA**: Animal health service (tuberculosis/screwworm programs)
- **T-MEC**: Mexico-US-Canada trade agreement (USMCA)
- **SSPi**: Sistemas Silvopastoriles Intensivos (intensive silvopastoral systems with Leucaena leucocephala at 40,000-53,000 plants/ha, 6.0 kg/ha seeding rate based on 18,000 seeds/kg, 85% germination, 90% survival rates) - $55,573/ha recommended scenario with 50% credit financing model
- **GBG**: Gusano Barrenador del Ganado (screwworm)
- **UPP**: Unidades de Producción Pecuaria (livestock production units)
- **FOFAY**: Fideicomiso Fondo de Fomento Agropecuario Yucatán (operational financing mechanism)
- **CESO**: Certificación Sanitaria Online (APHIS-USDA digital traceability platform)
- **SIAP**: Servicio de Información Agroalimentaria y Pesquera (official livestock statistics)
- **UGROY/UGRY**: Regional cattle associations (Oriente/Centro) for Pareto-based territorial focusing

## Project-Specific Patterns

### Multi-Agency Coordination
- Federal-state-producer tripartite governance structure with 8-person technical team
- International coordination with APHIS-USDA for sanitary protocols and digital certification
- Technical committee structure with program manager as technical secretary
- Pareto-based territorial focusing: 80% resources in 11 municipalities (10.4% territory = 80.3% cattle concentration)

### Performance Metrics Framework
- Physical targets: cattle population (605K → 1,005K head), land conversion (6,000 hectares SSPi), 1,320 UPP transformed
- Financial targets: $150M+ USD annual exports by 2030, $1,087.9M total investment execution with hybrid financing
- Economic viability: Beef calf weaning model with 4.0:1 credit payment capacity ratio (+1,167% productivity increase)
- Environmental targets: 765,000 ton CO₂eq carbon capture via intensive silvopastoral systems
- Social inclusion: ≥35% women and youth beneficiaries with technical assistance via FOFAY
- Technical targets: 250M sterile flies/week production capacity, T-MEC certification compliance

### Risk Management Approach
- Climate resilience through parametric insurance and scientifically-validated silvopastoral design
- Sanitary risk mitigation via sterile fly plant and intensive APHIS technical support
- Budget security through gubernatorial commitment letters and FOFAY fiduciary management
- Scientific validation through transparent calculation memories and APA citation system

## Development Workflow

### Document Generation
- Use institutional templates with NO BRANDING/LOGOS as independent consultant work for SEDER Yucatán
- **AUTHORSHIP**: All documents prepared by MVZ Sergio Muñoz de Alba Medrano, Independent Consultant, commissioned by SEDER Yucatán
- **MANDATORY**: Compile all LaTeX documents twice (pdflatex) to properly populate table of contents and cross-references
- Include PDF and Markdown versions of all strategic documents with complete scientific rigor
- Maintain Spanish language for official documents with technical English terms where appropriate
- Implement comprehensive APA citation system with numbered superscript references

### Python Data Analysis Workflow
- **Primary Tools**: pandas, PyPDF2, re for data extraction and analysis
- **Base Path Convention**: Use relative paths from project root for cross-platform compatibility
- **SIAP Data Integration**: Load livestock census from `DOCS REFERENCIA/2025. padron ganadero nacional yucatan detallado por municipios.csv`
- **Data Cleaning Protocol**: Remove quotes and commas from numeric columns, convert to integers for calculations
- **Budget Verification**: Cross-reference macro-project totals with individual component calculations
- **PDF Text Extraction**: Use PyPDF2 for mining scientific literature and extracting quantitative data
- **Pareto Analysis**: Implement 80/20 rule for territorial focusing (top 11 municipalities = 80.3% cattle concentration)

### Planning Documents
- 5-year strategic timelines with annual milestones and Gantt chart integration
- Detailed budget breakdowns by component and funding source with transparent calculation memories
- Governance matrices defining roles and responsibilities across federal/state/producer levels
- Program manager structure: 8-person technical team with $52.8M operational budget via FOFAY
- Territorial focusing based on Pareto analysis: 11 priority municipalities for maximum impact efficiency

### Scientific Documentation Standards
- All quantitative claims must include transparent calculation methodologies in formal annexes
- Carbon capture calculations based on validated SSPi research (765,000 ton CO₂eq over 5 years)
- Technical package specifications with detailed cost justifications ($12,100/ha SSPi standard, optimized through scientific seed calculation methodology)
- Performance indicators with baseline data from official SIAP sources (2014-2023 time series)
- Risk assessment matrices with mitigation strategies for each component
- Multidisciplinary analysis integration: territorial impacts (Pareto analysis), sanitary (binational TBC protocol APHIS-USDA/SENASICA), environmental (GHG reduction), economic (tripartite financing)
- Specific risk and mitigation section (climate vulnerability, cattle rustling, etc.)
- Traceability and digitalization emphasis: SINIIGA/SINIDA integration, official ear tags, CESO platform, T-MEC export benefits
- Iterative reviews with Mexican grammar correctors and expert validation (INIFAP, UADY)
- Audience adaptation: emphasize ROI for investors, regulatory alignment for authorities, include glossary when necessary
- **Revision Standards**: Conduct iterative reviews with Mexican Spanish grammar correctors and expert validation from INIFAP, UADY
- **Quality Control**: Correct accents, orthography, repetitions; ensure smooth transitions between sections
- **Audience Targeting**: For investors emphasize ROI metrics, for authorities highlight regulatory compliance, include technical glossaries when necessary

When working with this codebase, prioritize understanding the integrated nature of the six components and their interdependencies. The program manager role serves as the technical coordinator for federal execution across all components simultaneously, not as separate projects. All work must maintain scientific rigor with full traceability of data sources and calculation methodologies.