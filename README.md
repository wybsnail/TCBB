# AntibodyFlow (ABFlow): Normalizing Flow for Antibody CDR Loop Design

**AntibodyFlow (ABFlow)** is a 3D **normalizing flow** framework for *de novo* antibody CDR loop design.  
ABFlow performs **one-shot** generation of (i) a rotation/translation-invariant **pairwise distance matrix** and (ii) the corresponding **amino-acid sequence** conditioned on that geometry, with explicit **constraint learning** and **constrained coordinate reconstruction** to improve structural validity.

> This repository provides code for training, inference, evaluation, and reproducing the main results in our paper.

---

## Highlights

- **Two-stage generation**
  - **Distance matrix flow**: generate pairwise distances \(D\) (invariant to SE(3) transforms).
  - **Conditional amino-acid flow**: generate sequence \(S\) conditioned on \(D\).
- **Constraint mechanisms**
  - **Constraint learning** during training to encourage valid distance matrices.
  - **Constrained 3D coordinate generation** during inference to reconstruct coordinates \(G\) satisfying geometric constraints.
- **Targets**
  - CDR **H1**, **H2**, **H3** loops (modeled separately).

---

## Paper

**Normalizing Flow Model for Designing Antibody Complementarity-Determining Regions**  
Yanbo Wang, Bohao Xu, Wenyu Chen, Xiaoqin Yu, Shimin Shan.

If you use this code, please cite:

```bibtex
@article{wang_antibodyflow,
  title   = {Normalizing Flow Model for Designing Antibody Complementarity-Determining Regions},
  author  = {Wang, Yanbo and Xu, Bohao and Chen, Wenyu and Yu, Xiaoqin and Shan, Shimin},
  journal = {TBD (TCBB submission)},
  year    = {2026}
}
