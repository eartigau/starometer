# Prompt Memory - mdwarfometer

This file is a persistent in-folder memory of project prompts and key decisions.
Append new entries each work session.

## 2026-04-02
- Prompt: Build an HTML document with embedded Python code for an M-dwarf properties tool.
- Requirements captured:
  - Input field for object name.
  - Resolve with SIMBAD.
  - Import parallax and G/J/H/K magnitudes.
  - If data is missing, show message and allow manual input.
  - Keep a permanent memory of prompts in-folder for this multi-day project.
- Implementation started in index.html (Phase 1).
- Notes:
  - Current approach uses PyScript + SIMBAD TAP query from browser.
  - May require local serving due browser CORS restrictions.

- Bugfix note:
  - SIMBAD TAP 400 for GL699 was caused by selecting `id.main_id` (invalid column in `ident`).
  - Fixed by selecting `b.main_id` from `basic`.

- UI formatting update:
  - Bandpass labels are now italicized in the UI (<em>G</em>, <em>J</em>, <em>H</em>, <em>K</em>).
  - Units are displayed in square brackets (for example [mas], [mag]).

- Metallicty module start:
  - Added photometric [Fe/H] estimate in the web tool.
  - Implemented using a Bonfils et al. (2005) style relation based on M_K and (V-K).
  - Added V magnitude fetch and manual-input support because this calibration requires V and K.

## 2026-11-11
- Prompt: "that app fails, we should fix it".
- Cause: the CDS (SIMBAD, VizieR) went offline after a cybersecurity incident (cds.unistra.fr, 2026-11-10); the first SIMBAD query failed ("Failed to fetch").
  ESA's Gaia archive and the NASA Exoplanet Archive also refuse browser requests (no CORS header), so they cannot replace it.
- Fix: SIMBAD asked at the CDS, then its mirrors at the CfA (simbad.cfa.harvard.edu) and IDIA (simbad.idia.ac.za); VizieR, then GAVO's TAP
  (dc.g-vo.org: gaia.dr3lite, wise.main), which answers browsers; the service that answered is asked first afterwards. GAVO wants LANG=ADQL in capitals.
- Gaia DR3 astrophysical parameters (GSP-Phot, FLAME) only come from ESA, blocked by CORS: AFGK stars fall back to the Pecaut-Mamajek sequence.
- SIMBAD references query fixed: its ADQL wants r."year" selected and ORDER BY "year" (it failed at the CDS too; the list was empty).
- Formula fixes, checked against the papers (in ~/Documents/publications):
  - telluric window: the star's lines sit at RV - BERV from Earth, not RV + BERV (the windows were those of the opposite season);
    GJ 3470 now gives 5 Sep to 2 Dec, astropy's BERV at La Silla 8 Sep to 6 Dec.
  - Mann et al. (2015, erratum ApJ 819, 87) radius with [Fe/H]: the polynomial times (1 + 0.04458 [Fe/H]), not plus 0.04458 [Fe/H].
  - Duque-Arribas et al. (2023, ApJ 944, 88): their published Eq. 4 (Table 4 row 1, in W1-W2, BP-RP, M_G; 0.089 dex), with their
    calibration ranges (-0.10 <= W1-W2 <= 0.24, 1.85 <= G-J <= 3.10); the old formula (in M_Ks) came from a 2021 poster.
- The same relations, corrected, feed the star summary of lbl_gui's Data Explorer (lbl-pca2d, lbl/gui/starinfo.py).
