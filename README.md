# lemaitre.initial_data (LM-initial-data)

The **initial-data** domain of the [Lemaitre](https://github.com/LemaitreModels/Lemaitre)
package family: certified, differentiable, **parametric** binary-black-hole
initial data.

This repository is the *umbrella*. It owns the `lemaitre.initial_data` namespace
level and ships no science — the models live in the two submodules below, each
its own repository and its own installable distribution.

```python
import lemaitre as lm

lm.initial_data.conformally_flat    # the published Bowen–York puncture model
lm.initial_data.curved              # its non-conformally-flat successor
```

## The two puncture models

### `conformally_flat` — [`LMID-conformally-flat-puncture`](LMID-conformally-flat-puncture)

Distribution `lemaitre-initial-data-conformally-flat`. **The paper package.**

Certified, differentiable, parametric reduced-order model of the constraint
solve for quasi-circular **Bowen–York** punctures, up to the 8-D general-spin
model θ₈ = (b, q, χ_A, χ_B): a spectral xCFC solver on the Ansorg–Brügmann–Tichy
prolate chart, matrix-free Newton–Krylov, and a Smolyak/Hermite/POD parameter-space
ROM exposing `solve(θ, guess)` and the tangent `dU/dθ`. Ships `paper/` — the code
and the paper together.

### `curved` — [`LMID-curved-puncture`](LMID-curved-puncture)

Distribution `lemaitre-initial-data-curved`. **Skeleton — no physics yet.**

The non-conformally-flat successor: the same ABT chart, the same Newton–Krylov
solver, and the same parametric layer, with the conformally flat background
replaced by an attenuated superposition of quasi-isotropic conformally-**Kerr**
and Lorentz-boosted-Schwarzschild 3-metrics. The motivation is spin: above
χ ≈ 0.93 conformally flat data does not exist at all, which is the published
model's own stated limitation. It reuses `conformally_flat` directly — the chart,
the Newton–Krylov solver and the ROM — and so depends on it.

## Install

```bash
E="--config-settings editable_mode=compat"
pip install -e . $E                                  # this umbrella (pulls `lemaitre`)
pip install -e LMID-conformally-flat-puncture $E     # the published model
pip install -e LMID-curved-puncture $E               # the successor skeleton

python -c "import lemaitre as lm; lm.initial_data.conformally_flat"
```

The umbrella depends only on the `lemaitre` core. The solver stack (`jax`,
`numpy`, `scipy`, `matplotlib`) comes with whichever model you install; both are
self-contained beyond it, enforced by a test guard.

Each submodule builds, tests and releases on its own — see its `README.md` for
the acceptance suite and, for `conformally_flat`, the paper-reproduction targets.

## License

GPL-3.0 (see `LICENSE`).
