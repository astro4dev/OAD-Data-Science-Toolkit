## This a short schema browser for the fields in the catalogue.

| Column          | Description    |
|-----------------|----------------|
| mjd             | SDSS-DR7 modified jullian day for the spectroscopic observation|
| plate           | SDSS-DR7 plate for the spectroscopic observation|
| fiber_id        | SDSS-DR7 fiber indentification for the spectroscopic observation|
| xx_BPT_WHAN     | BPT and WHAN x axis: log [NII]/H_alpha - output from STARLIGHT|
| yy_BPT          | BPT y axis: log [OIII]/H_beta - output from STARLIGHT  |
| yy_WHAN         | WHAN y axis: EW(H_alpha) - output from STARLIGHT|
| BPT_class       | BPT classes: Star-forming (SF), Composite, Active Galactic Nuclei (AGN)|
| WHAN_class      |  WHAN classes: Star-forming (SF), weak AGN (wAGN), strong sAGN (sAGN), retired/passive (retired)|
| GMM_class_4     |  Gaussian Mixture Model solution with 4 Gaussian components (GCs).|
| pGC1            |  Probability to belong to GC1|
| pGC2            |  Probability to belong to GC2|
| pGC3            |  Probability to belong to GC3|
| pGC4            |  Probability to belong to GC4|
