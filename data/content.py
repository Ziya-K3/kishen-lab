"""Public record of the Kishen Lab, structured for the site."""

LAB = {
    "name": "Kishen Lab",
    "line": "Integrating science with clinical practice",
    "place": "Faculty of Dentistry, University of Toronto",
    "room": "Lab 510A",
    "street": "124 Edward Street",
    "city": "Toronto, Ontario, Canada M5G 1G6",
    "email": "anil.kishen@utoronto.ca",
    "phone": "+1 416 864 8224",
    "phone_href": "tel:+14168648224",
    "maps": "https://maps.google.com/?q=124+Edward+Street+Toronto+ON+M5G+1G6",
    "source": "https://thekishenlab.org/",
}

STATS = [
    {"value": 250, "suffix": "+", "label": "Journal articles"},
    {"value": 24, "suffix": "", "label": "Book chapters"},
    {"value": 3, "suffix": "", "label": "Books"},
    {"value": 10000, "suffix": "+", "label": "Citations"},
    {"value": 20, "suffix": "+", "label": "Years of the lab"},
]

PILLARS = [
    {
        "num": "01",
        "slug": "regenerative",
        "title": "Regenerative endodontics",
        "summary": "3D organoid models and engineered scaffolds for pulp and root regeneration, read through cell–cell and neuro-immune crosstalk.",
        "points": [
            "Apical papilla organoids and the cellular conversations that build a root",
            "Scaffolds, including human amniotic membrane matrix, for dental pulp regeneration",
            "Guidance for how biomaterials should be tested before anyone claims regeneration",
        ],
    },
    {
        "num": "02",
        "slug": "biomaterials",
        "title": "Biomaterials and nanotechnology",
        "summary": "Nanocomplexes and bioactive glasses tuned for antibacterial effect, mechanical recovery, and healing inside the tooth.",
        "points": [
            "Chitosan–hydroxyapatite nanocomplexes for dentin conditioning and sealer modification",
            "Bioactive glass added to hydraulic calcium silicate cements",
            "Nanoparticles that reverse disease-driven changes in hard tissue, toughen it, quiet proteases, and induce biomineralization",
        ],
    },
    {
        "num": "03",
        "slug": "immunology",
        "title": "Immunology and host–pathogen interaction",
        "summary": "How inflammation, infection, and repair are negotiated — and how intracanal medicines can modulate that response instead of only killing bacteria.",
        "points": [
            "Macrophage–fibroblast crosstalk in infected, hyperglycemic wounds",
            "In vitro disease models that score therapeutic effect quantitatively",
            "Local immunomodulation in apical periodontitis",
        ],
    },
    {
        "num": "04",
        "slug": "biomechanics",
        "title": "Hard-tissue biomechanics",
        "summary": "Optical interferometry at high resolution, under conditions that resemble the mouth, to map how dentin and bone actually carry load.",
        "points": [
            "Structure–function relationships in dento-osseous tissues",
            "Miniaturized models of biomechanical response, fluid dynamics, and drug delivery",
            "Pericervical dentin metrics from radiographs and CBCT",
        ],
    },
]

TRANSLATIONS = [
    {
        "title": "Tooth-sensitivity varnish",
        "detail": "A nanotechnology varnish for dentin hypersensitivity, carried into a product collaboration as UNO Gel.",
    },
    {
        "title": "Antibacterial oral-health varnish",
        "detail": "Surface treatments aimed at biofilm, not only at the symptoms biofilm leaves behind.",
    },
    {
        "title": "Chronic wound strategy",
        "detail": "A self-limiting host response for biofilm-mediated wounds, built for a world where antibiotics are not enough.",
    },
    {
        "title": "Root canal solutions",
        "detail": "Light, microbubbles, nanoparticles, and intracanal medicines designed to disinfect and then let tissue recover.",
    },
]

BASIC = [
    {
        "title": "Chronic wounds and tissue modulation",
        "body": "Repair is a negotiation among matrix, resident cells, and immune cells. More than 90% of chronic oral wounds are held open by biofilm, and antibiotics often cannot clear it. The lab’s nanoparticles are built to do several jobs at once: reverse disease-driven change in hard tissue, raise fracture toughness, inactivate host proteases, and induce biomineralization. The aim is a regulated host response — a practical answer to antibiotic resistance.",
    },
    {
        "title": "Host signalling in bacteria-mediated infection",
        "body": "Endogenous cells and immune cells trade mediators that tip a tissue toward health or disease. The lab builds in vitro models of that exchange, with microbial and non-microbial triggers, and assays that read therapeutic effect both by the numbers and by the biology.",
    },
    {
        "title": "Hard-tissue biomechanics",
        "body": "Optical interferometry gives a high-resolution look at dental hard tissue under conditions that resemble function. The work has traced distinct structure–function relationships in dento-osseous tissues, and miniaturized models for load, fluid flow, and drug delivery.",
    },
]

IMPACT = (
    "The nanotherapeutics developed here are meant to become the basis for preventing and treating "
    "bacteria-driven dental disease and chronic wounds. The same program gives biomaterials scientists, "
    "oral biologists, and industry two things they rarely get together: a clearer picture of health versus "
    "disease, and higher-throughput ways to test medicines. Around that science is a mentored, multidisciplinary "
    "training ground for the next leaders in oral health and chronic wound research."
)

ABOUT = {
    "kicker": "Engineering marvels of biology",
    "lead": (
        "Kishen Lab works at the front of endodontics, oral biology, and regenerative dentistry. "
        "Scientists, clinicians, engineers, and trainees come here from across the world to take on "
        "problems that a drill-and-fill habit cannot answer."
    ),
    "paragraphs": [
        "Under Dr. Anil Kishen, the group joins dental biology, biomaterials, immunology, and digital health. The mission is the gap between a laboratory finding and a clinical solution. Fundamental research, read against what actually happens in a mouth, can change how dental disease is prevented, diagnosed, and treated.",
        "The work runs from bio-inspired materials that resist infection and support regeneration, to nanotherapies and diagnostic tools. It is translational, and it is patient-centred.",
        "The lab is also a room where ideas get argued with, collaborations start, and future leaders are trained. Curiosity, rigor, and ethical responsibility are the house rules. International collaborators and industry partners are how a result leaves the bench and reaches a clinic.",
    ],
    "question": (
        "The tooth and its supporting tissues are built for mechanical work while living in a crowd of "
        "opportunistic microbes. Layered immune responses protect them, and those same responses decide "
        "how tissue repairs after treatment. Biomaterials have been the default for infected dental tissue "
        "for a very long time. The lab asks whether that is the right strategy for an organ this biologically "
        "adapted — and whether the body’s own capacity to function and heal can be recruited instead."
    ),
}

DIRECTOR = {
    "name": "Anil Kishen",
    "credentials": "BDS, MDS, PhD",
    "role": "Principal investigator",
    "titles": [
        "Professor and Canada Research Chair (Tier 1) in Oral Health Nanomedicine",
        "Associate scientist, Department of Dentistry, Mount Sinai Hospital",
        "Researcher, Wellman Center for Photomedicine, Massachusetts General Hospital",
    ],
    "editorial": [
        "Associate Editor, Journal of Endodontics (Elsevier)",
        "Associate Editor, Frontiers in Dental Medicine",
        "Section Editor, Clinical Oral Investigations (Springer)",
        "Associate Editor, BMC Microbiology",
    ],
    "photo": "images/anil-banner.jpg",
    "portrait": "images/anil-headshot.jpg",
    "bio": [
        "Dr. Anil Kishen is a clinician-scientist whose work crosses endodontics, pulp biology, nanotechnology, and biomedical engineering. He has authored more than 250 journal articles, 24 book chapters, and three books, with over 10,000 citations.",
        "The through-line is nanoparticle-guided therapy, bioactive nanomaterials that preserve dental tissue, and the biomechanics of dentin and endodontic cavities. He has also led international work on how dental research is reported, including PRIASE, so methods can be judged and repeated.",
        "He has mentored graduate students and postdoctoral fellows across clinical and engineering disciplines. Earlier appointments include the National University of Singapore and Nanyang Technological University. The standard he sets for the lab is straightforward: innovation, rigorous science, mentorship, and partnerships that turn a result into care.",
    ],
}

CURRENT = [
    {
        "name": "Prabha Lal",
        "role": "Postdoctoral research associate",
        "project": "Characterizing multispecies biofilm and host responses",
        "photo": "images/prabha.jpeg",
    },
    {
        "name": "Fang-Chi Li",
        "credentials": "DDS, MSc, PhD",
        "role": "Postdoctoral fellow",
        "project": "Apical papilla organoids and cellular crosstalk",
        "photo": "images/fangchi.png",
    },
    {
        "name": "Fardad Asghari Zadeh",
        "role": "Doctor of Dental Surgery",
        "project": "Cellular crosstalk underlying root resorption",
        "photo": "images/fardad.jpeg",
    },
    {
        "name": "Shivam Sharma",
        "role": "PhD student, Biotechnology",
        "project": "A heterogeneous cell-based model of the diabetic wound, and therapeutics for it",
        "photo": "images/shivam.jpeg",
    },
    {
        "name": "Nandita Menon",
        "role": "PhD student, Chemical Engineering",
        "project": "Modeling neurogenic inflammation",
        "photo": "images/nandita.png",
    },
    {
        "name": "Tanvi Sharma",
        "role": "Doctor of Dental Surgery",
        "project": "Mechanical testing of endodontic sealers",
        "photo": "images/tanvi.jpeg",
    },
    {
        "name": "Lauren Rotondi",
        "role": "Doctor of Dental Surgery",
        "project": "Integrin and cadherin in stem cells from the apical papilla, and their crosstalk with macrophages",
        "photo": "images/lauren.jpg",
    },
    {
        "name": "Shahin Afarin",
        "role": "PhD student",
        "project": "Organ-on-a-chip as a multi-organ approach",
        "photo": "images/shahin.jpg",
    },
    {
        "name": "Emma Afsa",
        "role": "Doctor of Dental Surgery",
        "project": "Crack propagation and micro-CT analysis of natural teeth",
        "photo": "images/emma.jpeg",
    },
]

ALUMNI = [
    {
        "id": "postdoc",
        "label": "Postdoctoral fellows",
        "people": [
            "Shi Zhilong, PhD (Chemical Engineering)",
            "Saji George, BSc, MSc, PhD",
            "Annie Shrestha, BDS, MSc, PhD",
            "Himani Kukreti, PhD (Immunology)",
            "Kamna Singh, PhD (Microbiology)",
        ],
    },
    {
        "id": "phd",
        "label": "Doctoral students",
        "people": [
            "Saji George, BSc, MSc (Biotechnology)",
            "Chee Peng Sum, BDS, MSc",
            "Xu Zhang, MTech (Chemical Engineering)",
            "Annie Shrestha, BDS, MSc",
            "Suja Shrestha, MSc (Chemistry), PhD",
            "Alice Fang-Chi Li, BDS, Dip Endo",
            "Arwa Bafail, BDS, FDSRCS (Edinburgh), co-supervisor",
            "Hebatullah Hussein, BDS, MDS, PhD",
            "Rajeshwari Siddappa, BDS, MDS (Periodontics), PhD",
        ],
    },
    {
        "id": "exchange",
        "label": "Exchange students",
        "people": [
            "Aldo del Carpio Perochena, PhD, University of São Paulo",
            "Ewa Rzad, PhD, Jagiellonian University",
            "Laura Voogt, MS, University of Groningen",
            "Tatiana Ramireza, PhD, University of Costa Rica",
            "Chen Zhenning, PhD, Southeast University",
            "Sera Lee, University of Hong Kong",
            "Tim Clair, University of Western Australia",
            "Jie Xong, PhD, Natural Science Foundation of China",
            "Cristiane Duque, UNESP, Brazil",
        ],
    },
    {
        "id": "msc",
        "label": "Master’s students",
        "people": [
            "Adeela Rafique, BDS, MSc (Research)",
            "Megha Haridas Upadya, BDS, MSc (Research)",
            "Shibi Mathew, BSc Microbiology, MSc (Research)",
            "Annie Shrestha, BDS, MSc (Research) and specialty",
            "Andrew Halford, DDS, MSc specialty",
            "Luis Da Silva, DDS, MSc specialty",
            "Anousheh P., DDS, MSc specialty",
            "Gillian Layton, DDS, MSc specialty",
            "Arezou Ossareh, MSc (Research)",
            "Andrei Ionescu, MSc specialty",
            "Helena Lim, MSc specialty",
            "Craig Bellamy, MSc specialty",
            "Nghia Nguyen, MSc specialty",
            "Anam Hashmi, MSc (Research)",
            "Bobby Nadeau, MSc specialty",
            "David Harris, MSc specialty",
            "Gillian Landzberg, MSc specialty",
            "Fang-Chi Li, MSc specialty",
            "Aldo Del Carpio-Perochena, MSc specialty",
            "Dani Stein, MSc Endodontics",
            "Emily Bishop, MSc Endodontics",
            "Armin M. Souzani, MSc Dentistry",
        ],
    },
]

PAPERS = [
    {
        "year": 2025,
        "title": "Dysfunctional crosstalk between macrophages and fibroblasts under LPS-infected and hyperglycemic conditions in diabetic wounds",
        "authors": "Sharma S, Kishen A",
        "journal": "Scientific Reports",
        "meta": "15(1), 17233",
        "theme": "immunology",
        "doi": "10.1038/s41598-025-00673-4",
        "summary": "In high glucose and bacterial challenge, macrophages lock into an inflammatory state and fibroblasts stop migrating. Paracrine signals make this worse; direct contact is gentler. A map for immunomodulatory wound therapy.",
        "figure": "images/fig-wound.png",
        "featured": True,
    },
    {
        "year": 2025,
        "title": "Investigation of the effect of addition or replacement of bioactive glass in hydraulic calcium silicate cement",
        "authors": "Koutroulis A, Menon N, Kapralos V, Kishen A, Sunde PT, et al.",
        "journal": "Dental Materials",
        "meta": "41(9), 1067–1079",
        "theme": "biomaterials",
        "doi": "",
        "summary": "What happens to chemistry, antibacterial effect, and biology when bioactive glass is added to, or substituted into, a radiopacified tricalcium silicate cement.",
        "figure": "images/fig-glass.jpg",
        "featured": True,
    },
    {
        "year": 2025,
        "title": "Clinical and preclinical postgraduate training in endodontic education: a transnational exploratory survey",
        "authors": "Nagendrababu V, Gopinath VK, Nassar M, Abbott PV, Duncan HF, et al.",
        "journal": "International Dental Journal",
        "meta": "75(4), 100861",
        "theme": "education",
        "doi": "",
        "summary": "A worldwide look at what endodontic postgraduate programs actually teach, in the clinic and before students reach it.",
        "figure": "images/fig-training.jpg",
        "featured": True,
    },
    {
        "year": 2025,
        "title": "Development of a Core Outcome Set in Endodontics (COS-ENDO): Part 1 — general methods",
        "authors": "Azarpazhooh A, Zanjir M, Cardoso E, Harman NL, Kishen A, Shah PS, et al.",
        "journal": "Journal of Endodontics",
        "meta": "51(4), 401–411",
        "theme": "education",
        "doi": "10.1016/j.joen.2025.01.008",
        "summary": "Methods for a core outcome set covering nonsurgical treatment, surgery, vital pulp therapy, apexification, and regenerative endodontics. Patients, clinicians, and researchers rated outcomes together.",
        "featured": False,
    },
    {
        "year": 2025,
        "title": "COS-ENDO: Part 4 — vital pulp therapy",
        "authors": "Zanjir M, Cardoso E, Harman NL, Khansari A, Jafarzadeh H, Kishen A, et al.",
        "journal": "Journal of Endodontics",
        "meta": "2025",
        "theme": "education",
        "doi": "",
        "summary": "The outcomes that should be reported when a study claims to have saved living pulp.",
        "featured": False,
    },
    {
        "year": 2025,
        "title": "COS-ENDO: Part 5 — apexification and regenerative endodontics",
        "authors": "Zanjir M, Cardoso E, Harman NL, Kishen A, Azarpazhooh A, et al.",
        "journal": "Journal of Endodontics",
        "meta": "51(4), 457–472",
        "theme": "regenerative",
        "doi": "10.1016/j.joen.2025.01.012",
        "summary": "Agreed outcomes include tooth survival, pain, signs of infection, radiographic healing, continued root development, and adverse events.",
        "featured": False,
    },
    {
        "year": 2025,
        "title": "Unraveling the etiology and pathogenesis of multiple cervical root resorption",
        "authors": "Lin Y, Thumbigere-Math V, Kishen A, He J",
        "journal": "Journal of Endodontics",
        "meta": "51(6), 674–686",
        "theme": "immunology",
        "doi": "10.1016/j.joen.2025.02.012",
        "summary": "A scoping review of 101 patients and 921 teeth. Systemic disease and drugs that alter osteoclast function sit behind a large share of these cases.",
        "featured": False,
    },
    {
        "year": 2025,
        "title": "Guidance for evaluating biomaterials for dental pulp tissue engineering",
        "authors": "Rosa V, Cavalcanti BN, Nör JE, Kishen A, Duncan HF, Ferracane JL, Watts DC, et al.",
        "journal": "Dental Materials",
        "meta": "41(3), 248–264",
        "theme": "regenerative",
        "doi": "10.1016/j.dental.2024.12.003",
        "summary": "Pulp has to defend, feel, vascularize, and make dentin. This paper sets out how to test a material against that whole job, and how to report it so others can use the result.",
        "featured": False,
    },
    {
        "year": 2025,
        "title": "Impact of wine polyphenols on the inflammatory profile of induced apical periodontitis in rats",
        "authors": "Ricci R, de Moura Pereira B, Kishen A, et al.",
        "journal": "Journal of Endodontics",
        "meta": "2025",
        "theme": "immunology",
        "doi": "",
        "summary": "Diet-derived polyphenols, read against the inflammatory profile of apical periodontitis in an animal model.",
        "featured": False,
    },
    {
        "year": 2024,
        "title": "Pericervical dentin metrics in mandibular first molars determined with periapical radiography and CBCT",
        "authors": "Boveda C, Kishen A, Millan B, Camejo MV, Gomez-Sosa JF",
        "journal": "Journal of Endodontics",
        "meta": "2024",
        "theme": "biomechanics",
        "doi": "",
        "summary": "How much pericervical dentin is really there, and how two common imaging methods disagree about it.",
        "featured": False,
    },
    {
        "year": 2023,
        "title": "3D organoids for regenerative endodontics",
        "authors": "Li F-C, Kishen A",
        "journal": "Biomolecules",
        "meta": "2023",
        "theme": "regenerative",
        "doi": "",
        "summary": "Organoids as a way to study pulp and root regeneration without pretending a flat dish is a tooth.",
        "featured": True,
    },
    {
        "year": 2022,
        "title": "Impact of dentin conditioning and sealer modification with chitosan–hydroxyapatite nanocomplexes",
        "authors": "del Carpio-Perochena A, Nicholson E, Singh CV, Camilleri J, Kishen A",
        "journal": "Journal of Endodontics",
        "meta": "2022",
        "theme": "biomaterials",
        "doi": "",
        "summary": "Nanocomplexes used both to condition dentin and to modify sealer, aimed at the interface that usually fails.",
        "featured": False,
    },
    {
        "year": 2022,
        "title": "Methodological quality assessment criteria for laboratory-based studies",
        "authors": "Nagendrababu V, Abbott PV, Boutsioukis C, Duncan HF, Faggion CM, Kishen A, et al.",
        "journal": "International Endodontic Journal",
        "meta": "2022",
        "theme": "education",
        "doi": "",
        "summary": "A shared yardstick for judging whether a bench study in endodontics was done in a way others can trust.",
        "featured": False,
    },
    {
        "year": 2022,
        "title": "Human amniotic membrane extracellular matrix scaffold for dental pulp regeneration",
        "authors": "Bakhtiar H, Ashoori A, Rajabi S, Azarpazhooh A, Kishen A, et al.",
        "journal": "International Endodontic Journal",
        "meta": "2022",
        "theme": "regenerative",
        "doi": "",
        "summary": "A biological scaffold, derived from amniotic membrane, tested as a home for regenerating pulp.",
        "featured": False,
    },
    {
        "year": 2022,
        "title": "Assessing macrophage polarization in nanoparticle-guided wound repair",
        "authors": "Singh K, Ali A, Shrestha A, Magalhaes M, Kishen A",
        "journal": "Journal of Endodontics",
        "meta": "2022",
        "theme": "immunology",
        "doi": "",
        "summary": "How to tell whether a nanoparticle treatment has shifted macrophages toward repair rather than prolonged inflammation.",
        "featured": False,
    },
    {
        "year": 2022,
        "title": "Nanomaterials in endodontics",
        "authors": "Kishen A, Shrestha A",
        "journal": "Endodontic Advances and Evidence-Based Clinical Guidelines",
        "meta": "Book chapter, 2022",
        "theme": "biomaterials",
        "doi": "",
        "summary": "A clinical-facing synthesis of where nanomaterials actually stand in endodontic treatment.",
        "featured": False,
    },
    {
        "year": 2022,
        "title": "Local immunomodulatory effects of intracanal medications in apical periodontitis",
        "authors": "Hussein H, Kishen A",
        "journal": "Journal of Endodontics",
        "meta": "2022",
        "theme": "immunology",
        "doi": "",
        "summary": "Intracanal medicines considered as modulators of the host response, not only as antimicrobials.",
        "featured": False,
    },
]

THEMES = [
    ("regenerative", "Regenerative"),
    ("biomaterials", "Biomaterials"),
    ("immunology", "Immunology"),
    ("biomechanics", "Biomechanics"),
    ("education", "Methods & education"),
]

PATENTS = [
    {
        "title": "Medical and dental handpiece",
        "number": "US 11,191,428",
        "status": "Granted",
        "date": "7 December 2021",
        "holder": "SYACT, LLP",
        "inventors": "Chang, Bruder, Kuttler, Kishen",
        "summary": "A handpiece that can deliver light through a probe, drive that probe, or do both, at a treatment site.",
    },
    {
        "title": "Light-transmitting probe for root canal disinfection",
        "number": "US 11,090,135",
        "status": "Granted",
        "date": "17 August 2021",
        "holder": "SYACT, LLP",
        "inventors": "Bruder, Kuttler, Kishen",
        "summary": "A probe whose metallic sheath reflects light and releases it through apertures, combined with ultrasonic, sonic, or electric energy.",
    },
    {
        "title": "Photosensitising composition",
        "number": "US 10,568,961",
        "status": "Granted",
        "date": "25 February 2020",
        "holder": "Dentsply Sirona",
        "inventors": "Kishen, George",
        "summary": "An oxygen carrier, an oxidizing agent, and a surfactant, proportioned for treating conditions caused by microorganisms.",
    },
    {
        "title": "Activated micro-bubble root canal disinfection",
        "number": "US 9,987,200",
        "status": "Granted",
        "date": "5 June 2018",
        "holder": "SyACT, LLP",
        "inventors": "Kishen",
        "summary": "A photoactive solution followed by an oxygen-carrying micro-bubble solution, activated with sound and light inside a shaped canal.",
    },
    {
        "title": "Multi-functional micro- and nanoparticles for root canal therapy",
        "number": "University of Toronto applications",
        "status": "Applications",
        "date": "Filed from 2013",
        "holder": "Governing Council of the University of Toronto",
        "inventors": "Kishen, Shrestha",
        "summary": "Chitosan nanoparticles, optionally linked to photoactivatable compounds, for antibacterial effect, neutralizing bacterial byproducts, and strengthening the tissue–filling interface.",
    },
    {
        "title": "Endodontic restoration post",
        "number": "US application 2019/0151047",
        "status": "Application",
        "date": "Published 23 May 2019",
        "holder": "—",
        "inventors": "Bruder, Kuttler, Kishen",
        "summary": "A fiber-reinforced structural member that, with a post, forms a three-dimensional reinforcement for an endodontically treated tooth.",
    },
    {
        "title": "Delivery of particles in a root canal system",
        "number": "US application 2018/0049856",
        "status": "Application",
        "date": "Published 22 February 2018",
        "holder": "—",
        "inventors": "Ionescu, Kishen",
        "summary": "An intracanal electrode and an intraoral electrode create a field that helps move particles and reduce bacteria.",
    },
    {
        "title": "Fiber-optic biosensor",
        "number": "US application 2006/0177891",
        "status": "Application",
        "date": "Published 10 August 2006",
        "holder": "—",
        "inventors": "Kishen, Mechery, Lim, Asundi",
        "summary": "An unclad optical fiber with a coating that a target microbe metabolizes into a spectroscopic signal. Early coverage in the Straits Times and Lianhe Zaobao came from this line of work.",
    },
]

AWARDS = [
    {"year": 2023, "scope": "personal", "title": "CADR–ACFD National Dental Research Award", "detail": "Canadian Association of Dental Research and the Association of Canadian Faculties of Dentistry. For contribution, mentorship, and leadership at a Canadian university."},
    {"year": 2023, "scope": "personal", "title": "Dr. Lloyd and Mrs. Kay Chapman Chair in Clinical Science", "detail": "Named chair."},
    {"year": 2023, "scope": "team", "title": "University of Toronto 3MT, People’s Choice", "detail": "Principal supervisor."},
    {"year": 2023, "scope": "team", "title": "Journal of Endodontics awards for 2022", "detail": "Basic science biology; narrative review. Honorable mentions in technology, regenerative endodontics, and biology."},
    {"year": 2022, "scope": "personal", "title": "Stanford–Elsevier top 2% of scientists", "detail": "Field: dentistry."},
    {"year": 2022, "scope": "team", "title": "Journal of Endodontics, case reports and clinical techniques", "detail": "With an honorable mention in basic science technology."},
    {"year": 2022, "scope": "team", "title": "University of Toronto 3MT, People’s Choice", "detail": "Principal supervisor."},
    {"year": 2021, "scope": "personal", "title": "Louis I. Grossman Award, American Association of Endodontists", "detail": "For a body of published research that has made an extraordinary contribution to endodontology. Announced for 2021."},
    {"year": 2021, "scope": "team", "title": "Jean-Marie Laurichesse Research Award, IFEA", "detail": "International Federation of Endodontic Associations. Principal supervisor."},
    {"year": 2021, "scope": "team", "title": "CADR–NCOHR Award, senior basic science", "detail": "Principal supervisor."},
    {"year": 2021, "scope": "team", "title": "Journal of Endodontics, best basic science technology paper of 2020", "detail": "Principal supervisor."},
    {"year": 2021, "scope": "team", "title": "Pulp Biology and Regeneration Group travel award", "detail": "Principal supervisor."},
    {"year": 2020, "scope": "team", "title": "CADR–NCOHR Award, senior clinical science", "detail": "For 2019. Principal supervisor."},
    {"year": 2020, "scope": "team", "title": "Journal of Endodontics, best basic science technology paper of 2019", "detail": ""},
    {"year": 2019, "scope": "personal", "title": "George Hare Memorial Lectureship", "detail": "Canadian Academy of Endodontics, Mont-Tremblant."},
    {"year": 2019, "scope": "team", "title": "Hatton Award, first place", "detail": "CADR–NCOHR, senior basic science. Principal supervisor."},
    {"year": 2019, "scope": "team", "title": "AAE research award, oral presentations", "detail": "Montreal. Principal supervisor."},
    {"year": 2017, "scope": "team", "title": "AAE research award, first place oral", "detail": "New Orleans. Principal supervisor."},
    {"year": 2017, "scope": "team", "title": "Journal of Endodontics honorable mention, basic science technology", "detail": ""},
    {"year": 2016, "scope": "personal", "title": "W.W. Wood Award", "detail": "Canadian Faculty Association, for excellence in dental education."},
    {"year": 2016, "scope": "personal", "title": "Steven P. Chartan Memorial Lectureship", "detail": "Einstein Medical Center, Philadelphia."},
    {"year": 2016, "scope": "team", "title": "Journal of Endodontics, best basic science technology paper of 2015", "detail": ""},
    {"year": 2016, "scope": "team", "title": "AAE research awards", "detail": "San Francisco. Two projects. Principal supervisor."},
    {"year": 2015, "scope": "personal", "title": "Burroughs Wellcome Fund visiting scholarship", "detail": "Wellman Center for Photomedicine, Massachusetts General Hospital."},
    {"year": 2015, "scope": "personal", "title": "Edward C. Penick Endodontic Lectureship", "detail": "Baltimore."},
    {"year": 2015, "scope": "team", "title": "Journal of Endodontics, best basic science technology paper of 2014", "detail": "Plus an honorable mention in the same category."},
    {"year": 2015, "scope": "team", "title": "CADR–NCOHR, senior basic science, third place", "detail": "Team award."},
    {"year": 2015, "scope": "team", "title": "AAE research award", "detail": "Seattle. Principal supervisor."},
    {"year": 2014, "scope": "personal", "title": "AAE–Dentsply Research Excellence Award", "detail": "Principal investigator, University of Toronto."},
    {"year": 2014, "scope": "personal", "title": "Cover feature, Nanomedicine", "detail": "April 2014 issue."},
    {"year": 2014, "scope": "personal", "title": "Irving Naidorf Lectureship", "detail": "Columbia University."},
    {"year": 2013, "scope": "personal", "title": "Edgar D. Coolidge Lectureship", "detail": "Chicago."},
    {"year": 2013, "scope": "personal", "title": "Langham Endodontic Group Lectureship", "detail": "London."},
    {"year": 2013, "scope": "personal", "title": "Diplomate, Indian Board of Endodontics", "detail": ""},
    {"year": 2013, "scope": "team", "title": "AAE research award", "detail": "Honolulu. Principal supervisor."},
    {"year": 2013, "scope": "team", "title": "U of T Dental Student Society honorary member", "detail": "For contribution to undergraduate endodontic education."},
    {"year": 2012, "scope": "team", "title": "Jean-Marie Laurichesse Research Award, IFEA", "detail": "Principal supervisor."},
    {"year": 2012, "scope": "team", "title": "AAE research award", "detail": "Boston. Principal supervisor."},
    {"year": 2011, "scope": "team", "title": "AAE research award", "detail": "San Antonio. Principal supervisor."},
    {"year": 2009, "scope": "team", "title": "GC Dental Asia student research competition, second prize", "detail": "Chiang Mai. Principal supervisor."},
    {"year": 2008, "scope": "personal", "title": "Commentary in Nature Photonics", "detail": "“A new light in dentistry.” Nature Photonics 2, 705–707."},
    {"year": 2008, "scope": "team", "title": "Dentsply Student Clinician, second prize", "detail": "SEAADE–IADR, Manila. Principal supervisor."},
    {"year": 2004, "scope": "team", "title": "Singapore and Malaysian Endodontic Societies, first prize", "detail": "Principal supervisor."},
    {"year": 2002, "scope": "team", "title": "The Enterprise Challenge innovator award", "detail": "Team award, Singapore."},
    {"year": 2002, "scope": "team", "title": "Far Eastern Economic Review Asian Innovation Awards, finalist", "detail": "Hong Kong."},
    {"year": 2001, "scope": "personal", "title": "SPIE travel award", "detail": "International Society for Optics and Photonics."},
    {"year": 1997, "scope": "personal", "title": "Singapore Ministry of Education–NTU doctoral scholarship", "detail": "Nanyang Technological University."},
    {"year": 1996, "scope": "personal", "title": "Tamil Nadu State Dental Association research award", "detail": "Tiruchirappalli."},
    {"year": 1995, "scope": "personal", "title": "Federation of Operative Dentistry of India research award", "detail": "Calcutta."},
    {"year": 1994, "scope": "personal", "title": "Colgate-Palmolive research award", "detail": "Madras."},
]

NEWS = [
    {
        "date": "2025",
        "outlet": "Faculty of Dentistry",
        "title": "From the lab to the barn",
        "summary": "Nanoparticles built for the mouth show up in the care of an injured horse. The same tunable chemistry used for wounds does not stop at the oral cavity.",
        "href": "https://thekishenlab.org/from-the-lab-to-the-barn-how-dentistry-research-is-being-applied-beyond-the-mouth/",
        "featured": True,
    },
    {
        "date": "2025",
        "outlet": "Kishen Lab",
        "title": "Engage and inform: a transformative journey in scientific talks",
        "summary": "Dr. Kishen on the talk that taught him a hard lesson — friends who said the science was good and still understood none of it — and on what presentation owes an audience.",
        "href": "https://thekishenlab.org/engage-and-inform-through-impactful-presentations-my-transformative-journey/",
        "featured": True,
    },
    {
        "date": "AAE Communiqué",
        "outlet": "American Association of Endodontists",
        "title": "Catching up with a Canada Research Chair",
        "summary": "Tier 1 Canada Research Chair in oral health nanomedicine. Endodontics at the nanoscale, with consequences well beyond the canal.",
        "href": "https://thekishenlab.org/catching-up-with-canada-research-chair-tier-1-professor-anil-kishen/",
        "featured": False,
    },
    {
        "date": "Dental Tribune",
        "outlet": "Dental Tribune South Asia",
        "title": "Nanoparticle irrigation: more than canal disinfection",
        "summary": "An interview on microbiology, disinfection, biomechanics, and tissue engineering — and why irrigation with nanoparticles is a biological strategy, not a stronger bleach.",
        "href": "https://thekishenlab.org/interview-nanoparticle-irrigation-more-than-canal-disinfection-dr-anil-kishen/",
        "featured": False,
    },
    {
        "date": "15 November 2021",
        "outlet": "University of Toronto",
        "title": "Four graduates who stayed for research and teaching",
        "summary": "Hebatullah Hussein, Fang-Chi Li, Justin Bubola, and Nashat Cassim on building academic careers out of the faculty’s graduate programs.",
        "href": "https://thekishenlab.org/these-four-u-of-t-dentistry-graduates-set-their-sights-on-research-and-teaching/",
        "image": "images/news-grads.png",
        "featured": False,
    },
]

MEDIA = [
    {"year": "2001", "outlet": "Lianhe Zaobao", "title": "NTU invents a device to monitor oral bacteria in five minutes", "href": ""},
    {"year": "2002", "outlet": "The Straits Times", "title": "Fiber-optics sniff out bacteria fast", "href": ""},
    {"year": "2007", "outlet": "L’Information Dentaire", "title": "Mechanisms and risk factors for fracture-predilection areas in pulpless teeth", "href": ""},
    {"year": "—", "outlet": "APEX", "title": "Light proves to be an important weapon against bacteria", "href": ""},
    {"year": "2012", "outlet": "Journal of Endodontics", "title": "Interview on microbubble emulsion and chitosan nanoparticles", "href": ""},
    {"year": "2012", "outlet": "Journal of Endodontics", "title": "Interview on endodontic infection and photodynamic therapy", "href": ""},
    {"year": "2015", "outlet": "University of Toronto News", "title": "A television “no-no” opens the door for nanoparticle dental treatments", "href": ""},
    {"year": "2015", "outlet": "Electro Optics", "title": "A healthy dose of interferometry", "href": "http://www.electrooptics.com/features/feature.php?feature_id=377"},
    {"year": "2016", "outlet": "The Daily Beast", "title": "Bye bye brushing: nanoparticles are coming to save your teeth", "href": "https://www.thedailybeast.com/articles/2016/03/13/bye-bye-brushing-nanoparticles-are-coming-to-save-your-teeth.html"},
    {"year": "2016", "outlet": "Faculty of Dentistry", "title": "A dentistry startup takes on tooth sensitivity with nanotechnology", "href": "https://www.dentistry.utoronto.ca/news/dentistry-startup-solves-tooth-sensitivity-nanotechnology"},
    {"year": "2016", "outlet": "Impact Centre / Marketwired", "title": "Oral Antibacterials launches UNO Gel with Germiphene", "href": "http://www.marketwired.com/press-release/oral-antibacterials-inc-launches-uno-gel-dentin-hypersensitivity-collaboration-with-2170658.htm"},
    {"year": "2016", "outlet": "CDA OASIS", "title": "Dentistry startup solves tooth sensitivity", "href": "http://oasisdiscussions.ca/2016/12/15/uno/"},
    {"year": "2018", "outlet": "AAE Communiqué", "title": "Pathways for novel studies in endodontics", "href": "https://www.aae.org/specialty/2018/07/09/pathways-for-novel-studies-in-endodontics/"},
    {"year": "2019", "outlet": "Faculty of Dentistry", "title": "A bioactive nanosystem promotes regeneration after root canals", "href": "https://www.dentistry.utoronto.ca/news/bioactive-nanosystem-promotes-regeneration-after-root-canals"},
    {"year": "2019", "outlet": "University of Toronto News", "title": "Nanosystem promotes regeneration after root canals", "href": "https://www.utoronto.ca/news/u-t-researcher-develops-nanosystem-promotes-regeneration-after-root-canals"},
    {"year": "2019", "outlet": "Technology.org", "title": "Researcher develops a nanosystem that promotes regeneration after root canals", "href": "https://www.technology.org/2019/10/14/u-of-t-researcher-develops-nanosystem-that-promotes-regeneration-after-root-canals/"},
    {"year": "2019", "outlet": "Oral Health", "title": "U of T researcher develops nanosystem that promotes regeneration after root canals", "href": "https://www.oralhealthgroup.com/news/u-of-t-researcher-develops-nanosystem-that-promotes-regeneration-after-root-canals-1003945557"},
    {"year": "2020", "outlet": "CDA Essentials", "title": "New material may aid regeneration after root canals", "href": ""},
    {"year": "2020", "outlet": "Dental 360", "title": "Cover portrait and biography", "href": ""},
    {"year": "2020", "outlet": "Expertscape", "title": "World Expert in Endodontics — top 0.1% of scholars over ten years", "href": "https://www.expertscape.com/ex/endodontics"},
    {"year": "2020", "outlet": "American Association of Endodontists", "title": "AAE announces its award winners", "href": "https://www.aae.org/specialty/2020/01/17/american-association-of-endodontists-announces-its-2020-award-winners/"},
    {"year": "2020", "outlet": "Faculty of Dentistry", "title": "Anil Kishen honored by the American Association of Endodontists", "href": "https://www.dentistry.utoronto.ca/news/anil-kishen-honoured-american-association-of-endodontics"},
    {"year": "2023", "outlet": "American Association of Endodontists", "title": "Recipient of the CADR–ACFD National Dental Research Award", "href": "https://www.aae.org/specialty/dr-anil-kishen-chosen-as-recipient-of-cadr-acfd-national-dental-research-award-for-2023/"},
    {"year": "—", "outlet": "Faculty of Dentistry", "title": "Two faculty awards push new discoveries forward", "href": "https://www.dentistry.utoronto.ca/news/two-faculty-awards-push-compelling-new-discoveries-forward"},
]

TESTIMONIALS = [
    {
        "quote": "Seminal. This just blew me away. This might have been the best presented seminar I've been to at an annual session.",
        "by": "AAE 2015, post-lecture feedback",
    },
    {
        "quote": "I have marvelled at your knowledge of the subjects that you presented and wish you continued success in endodontics.",
        "by": "Franklin S. Weine",
    },
]

PARTNERS = [
    "University of Toronto",
    "Faculty of Dentistry",
    "Mount Sinai Hospital",
    "Canada Research Chairs",
    "Wellman Center for Photomedicine",
    "American Association of Endodontists",
    "Journal of Endodontics",
]

FUNDS = [
    {"name": "Natural Sciences and Engineering Research Council of Canada", "file": "images/fund-1.jpg"},
    {"name": "Canada Foundation for Innovation", "file": "images/fund-2.jpg"},
    {"name": "Foundation for Endodontics", "file": "images/fund-3.jpg"},
    {"name": "University of Toronto", "file": "images/fund-4.jpg"},
    {"name": "Ontario Centres of Excellence", "file": "images/fund-5.jpg"},
    {"name": "Mitacs", "file": "images/fund-6.jpg"},
]

COVERS = [
    {"file": "images/media-1.jpg", "caption": "Dental 360 cover, September 2020"},
    {"file": "images/media-2.jpg", "caption": "The Straits Times, 30 December 2002"},
    {"file": "images/media-3.jpg", "caption": "American Association of Endodontists, 2018"},
]

PAGES = [
    {
        "kind": "Page",
        "title": "About the lab",
        "href": "/about",
        "text": "mission clinician scientist engineering biology regenerative dentistry mentoring Toronto endodontics oral biology",
    },
    {
        "kind": "Page",
        "title": "Research themes",
        "href": "/research",
        "text": "regenerative endodontics organoid biomaterials nanoparticles immunology biofilm biomechanics interferometry patents wound chitosan bioactive glass",
    },
    {
        "kind": "Page",
        "title": "People",
        "href": "/people",
        "text": "Anil Kishen Canada Research Chair students postdoctoral alumni mentoring",
    },
    {
        "kind": "Page",
        "title": "Publications",
        "href": "/publications",
        "text": "papers journal articles COS-ENDO organoids macrophages citations",
    },
    {
        "kind": "Page",
        "title": "Awards",
        "href": "/awards",
        "text": "Grossman Award Wood Award Canada Research Chair Hatton CADR AAE lectureship",
    },
    {
        "kind": "Page",
        "title": "Media",
        "href": "/media",
        "text": "news nanoparticles horse interview Dental Tribune Straits Times UNO gel",
    },
    {
        "kind": "Page",
        "title": "Visit and contact",
        "href": "/contact",
        "text": "email phone Lab 510A 124 Edward Street Toronto prospective student collaboration",
    },
]
