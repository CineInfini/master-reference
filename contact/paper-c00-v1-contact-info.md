# PAPER-C00-v1: Contact Information & Affiliations
## Centralized Contact Details for All CineInfini Publications

**Version**: 1.0.0  
**Date**: 2026-04-02  
**Status**: CANONICAL REFERENCE for author information

---

## USAGE

All CineInfini papers (T01-T91, Nature Brief, etc.) reference this file for contact information. Update here once → propagates to all papers.

**LaTeX macro**:
```latex
\input{contact_from_C00}
% Provides: \AuthorName, \AuthorTitle, \AuthorEmail, \AuthorPhone, etc.
```

---

## AUTHOR INFORMATION

### Primary Author

**Name**: Dr. Salah-Eddine Benbrahim  
**Title**: Dr. (Doctoral degree)  
**Affiliation**: CineInfini Research  
**Specialization**: HPC Systems Architecture • Generative AI • Deterministic Cinematography

**LaTeX format**:
```latex
\author{Dr. Salah-Eddine Benbrahim}
\affiliation{CineInfini Research}
\email{benbrahim.salah.eddine.777@gmail.com}
```

---

## CONTACT DETAILS

### Email (Primary)
**Address**: benbrahim.salah.eddine.777@gmail.com  
**Usage**: All correspondence, manuscript submissions, reviewer communications

**LaTeX**:
```latex
\correspondence{benbrahim.salah.eddine.777@gmail.com}
```

### Phone
**Number**: +33 7 81 64 82 93  
**Format (international)**: +33 7 81 64 82 93  
**Format (national FR)**: 07 81 64 82 93  
**Country**: France (FR)

**LaTeX**:
```latex
\phone{+33~7~81~64~82~93}
```

### Mailing Address
**Address**: [TO BE PROVIDED IF NEEDED]  
**City**: [CITY]  
**Postal Code**: [CODE]  
**Country**: France

---

## ALTERNATIVE CONTACTS (IF NEEDED)

### Professional Email (if created)
**Email**: salah.benbrahim@cineinfini.ai  
**Status**: Currently using Gmail, this domain-based email can be created later

### ORCID
**ID**: 0009-0005-7050-4014  
**URL**: https://orcid.org/0009-0005-7050-4014  
**Status**: ✅ Registered and active

### LinkedIn
**URL**: [TO BE PROVIDED IF PUBLIC]

### GitHub
**Organization**: github.com/cineinfini  
**Personal**: [TO BE PROVIDED]

---

## INSTITUTIONAL AFFILIATIONS (PLANNED)

### Current
- **CineInfini Research** (Independent research project)

### Potential Future Affiliations
- University partnership (TBD)
- HPC center collaboration (TBD)
- Industry partnership (NVIDIA, AWS, etc.)

---

## CO-AUTHORS (IF APPLICABLE)

### Format for Multi-Author Papers

**Co-author 1** (example):
```latex
\author[1]{Dr. Salah-Eddine Benbrahim}
\author[2]{Co-Author Name}
\affil[1]{CineInfini Research, France}
\affil[2]{Institution Name, Country}
```

**Current**: All papers are single-author  
**Future**: May add co-authors for specialized papers (HPC, economics, film studies)

---

## CORRESPONDENCE AUTHOR

**For all papers**: Dr. Salah-Eddine Benbrahim

**LaTeX template**:
```latex
\correspondence{
  Dr. Salah-Eddine Benbrahim \\
  CineInfini Research \\
  Email: benbrahim.salah.eddine.777@gmail.com \\
  Phone: +33~7~81~64~82~93
}
```

---

## COMPETING INTERESTS STATEMENT

**Standard text** (all papers):
```
The author has no competing interests to declare. Intellectual property 
status, funding sources, and potential conflicts of interest are detailed 
in the CineInfini Intellectual Property Declaration (IP00 v1.0.0), publicly 
available at: https://github.com/cineinfini/master-reference/ip/PAPER-IP00-v1.0.0.md
```

**LaTeX**:
```latex
\competinginterests{
  The author has no competing interests to declare. IP status detailed in 
  IP00 v1.0.0 (https://github.com/cineinfini/master-reference/ip/PAPER-IP00-v1.0.0.md)
}
```

---

## FUNDING STATEMENT

**Current**: Self-funded research

**LaTeX**:
```latex
\funding{This research received no specific grant from any funding agency 
in the public, commercial, or not-for-profit sectors.}
```

**Future** (if grants obtained):
```latex
\funding{This work was supported by [GRANT NAME] (Grant No. [NUMBER]) 
from [AGENCY].}
```

---

## DATA AVAILABILITY STATEMENT

**Standard text** (all papers):
```
All data, code, and constants are available at: 
https://github.com/cineinfini/master-reference

Master Reference (M00): Constants and variables
Bibliography (T00): Centralized references
```

**LaTeX**:
```latex
\dataavailability{
  All data, code, and constants are available at: \\
  \url{https://github.com/cineinfini/master-reference}
  
  Master Reference (M00): Constants and variables \\
  Bibliography (T00): Centralized references
}
```

---

## ACKNOWLEDGMENTS (TEMPLATE)

**Standard acknowledgments**:
```
The author thanks [REVIEWERS/COLLEAGUES] for valuable feedback on 
earlier versions of this manuscript. Computational resources were 
provided by [CLOUD PROVIDER / HPC CENTER].
```

**For papers with specific contributions**:
```
The author acknowledges [NAME] for assistance with [SPECIFIC CONTRIBUTION], 
and [NAME] for discussions on [TOPIC].
```

---

## AUTO-GENERATED LATEX MACROS

### File: contact_from_C00.tex

```latex
% Auto-generated from PAPER-C00-v1
% DO NOT EDIT MANUALLY

% Author information
\newcommand{\AuthorName}{Dr. Salah-Eddine Benbrahim}
\newcommand{\AuthorTitle}{Dr.}
\newcommand{\AuthorFirstName}{Salah-Eddine}
\newcommand{\AuthorLastName}{Benbrahim}
\newcommand{\AuthorEmail}{benbrahim.salah.eddine.777@gmail.com}
\newcommand{\AuthorPhone}{+33~7~81~64~82~93}

% Affiliation
\newcommand{\AuthorAffiliation}{CineInfini Research}
\newcommand{\AuthorCountry}{France}

% Contact block
\newcommand{\ContactBlock}{%
  \textbf{Correspondence:} \\
  Dr. Salah-Eddine Benbrahim \\
  CineInfini Research \\
  Email: \href{mailto:benbrahim.salah.eddine.777@gmail.com}{benbrahim.salah.eddine.777@gmail.com} \\
  Phone: +33~7~81~64~82~93
}

% Competing interests
\newcommand{\CompetingInterests}{%
  The author declares patent applications related to Multi-Dimensional 
  Identity Cubes (MDIC) and deterministic video generation architectures. 
  Patent 1 (HW-SW Coupling) filed [DATE]. No financial competing interests.
}

% Data availability
\newcommand{\DataAvailability}{%
  All data, code, and constants are available at: 
  \url{https://github.com/cineinfini/master-reference}
}
```

---

## PYTHON SCRIPT: Generate Contact Macros

```python
#!/usr/bin/env python3
# File: scripts/generate_contact_macros.py

def generate_latex_contact_macros():
    """Generate LaTeX macros from C00 contact info."""
    
    contact = {
        'name': 'Dr. Salah-Eddine Benbrahim',
        'title': 'Dr.',
        'first': 'Salah-Eddine',
        'last': 'Benbrahim',
        'email': 'benbrahim.salah.eddine.777@gmail.com',
        'phone': '+33~7~81~64~82~93',
        'affiliation': 'CineInfini Research',
        'country': 'France'
    }
    
    macros = [
        "% Auto-generated from PAPER-C00-v1",
        "% DO NOT EDIT MANUALLY",
        "",
        "% Author information",
        f"\\newcommand{{\\AuthorName}}{{{contact['name']}}}",
        f"\\newcommand{{\\AuthorTitle}}{{{contact['title']}}}",
        f"\\newcommand{{\\AuthorFirstName}}{{{contact['first']}}}",
        f"\\newcommand{{\\AuthorLastName}}{{{contact['last']}}}",
        f"\\newcommand{{\\AuthorEmail}}{{{contact['email']}}}",
        f"\\newcommand{{\\AuthorPhone}}{{{contact['phone']}}}",
        "",
        "% Affiliation",
        f"\\newcommand{{\\AuthorAffiliation}}{{{contact['affiliation']}}}",
        f"\\newcommand{{\\AuthorCountry}}{{{contact['country']}}}",
    ]
    
    return "\n".join(macros)

if __name__ == "__main__":
    content = generate_latex_contact_macros()
    with open('contact_from_C00.tex', 'w') as f:
        f.write(content)
    print("✅ Contact macros generated: contact_from_C00.tex")
```

---

## USAGE IN PAPERS

### Example: T01-A.tex

```latex
\documentclass{article}
\input{contact_from_C00}  % Import contact macros

\begin{document}

\title{Digital Amnesia: A Theoretical Framework...}
\author{\AuthorName}
\affiliation{\AuthorAffiliation}

% ... paper content ...

\section*{Correspondence}
\ContactBlock

\section*{Competing Interests}
\CompetingInterests

\section*{Data Availability}
\DataAvailability

\end{document}
```

### Example: Nature Brief

```latex
\documentclass{nature}
\input{contact_from_C00}

% Header
Dr. Salah-Eddine Benbrahim
HPC Systems Architecture • Generative AI • Deterministic Cinematography

% ... manuscript ...

% Footer
Correspondence: \AuthorEmail
Competing interests: [See C00]
Data availability: github.com/cineinfini/master-reference
```

---

## MODIFICATION WORKFLOW

### Update Contact Information

**ÉTAPE 1**: Modify PAPER-C00-v1.md
```bash
vim PAPER-C00-v1-contact-info.md
# Change email, phone, affiliation, etc.
```

**ÉTAPE 2**: Regenerate LaTeX macros
```bash
python scripts/generate_contact_macros.py
# Output: contact_from_C00.tex (updated)
```

**ÉTAPE 3**: Recompile all papers
```bash
./scripts/recompile_all_papers.sh
# All papers now use new contact info
```

**Time**: 5 minutes vs 3 hours (manual update of 33 papers)

---

## VERSIONING

### Semantic Versioning

**Format**: `MAJOR.MINOR.PATCH`

**Examples**:
```
v1.0.0 (2026-04-02): Initial release
v1.0.1 (2026-05-01): Updated phone number
v1.1.0 (2026-06-01): Added ORCID ID
v2.0.0 (2027-01-01): Changed primary affiliation (breaking)
```

### Changelog

```markdown
## Version 1.0.0 (2026-04-02)
- Initial release
- Contact: benbrahim.salah.eddine.777@gmail.com
- Phone: +33 7 81 64 82 93
- Affiliation: CineInfini Research
```

---

## BENEFITS

### Centralization
- ✅ **Update once**: Change email → propagates to all 33 papers
- ✅ **Consistency**: Same format everywhere
- ✅ **No typos**: Generated macros prevent manual errors

### Time Savings
| Task | Without C00 | With C00 | Gain |
|------|-------------|----------|------|
| Update email | 2 min × 33 = 66 min | 5 min | **92%** |
| Add ORCID | 3 min × 33 = 99 min | 5 min | **95%** |
| Change affiliation | 5 min × 33 = 165 min | 10 min | **94%** |

### Professional
- ✅ Uniform contact blocks
- ✅ Complete metadata
- ✅ Easy to update as career progresses

---

## NEXT STEPS

### Immediate (Week 1)
- [ ] Create ORCID account (free, 5 min): https://orcid.org/register
- [ ] Reserve `salah.benbrahim@cineinfini.ai` domain email (optional)
- [ ] Setup GitHub organization: github.com/cineinfini

### Short-term (Month 1)
- [ ] Add ORCID to all papers
- [ ] Upload M00, T00 to GitHub
- [ ] Create professional email (if desired)

### Medium-term (Month 6)
- [ ] Explore university affiliation (adds credibility)
- [ ] Join professional associations (ACM, IEEE)
- [ ] Setup Google Scholar profile

---

**Last Updated**: 2026-04-02  
**Maintainer**: Dr. Salah-Eddine Benbrahim  
**Contact**: benbrahim.salah.eddine.777@gmail.com
