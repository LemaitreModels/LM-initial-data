# lemaitre.initial_data (LM-initial-data)

The **initial-data** domain of the [Lemaitre](https://github.com/LemaitreModels/Lemaitre)
package family: certified, differentiable, **parametric** binary-black-hole
initial data.

This repository is the *umbrella*. It owns the `lemaitre.initial_data` namespace
level and ships no science — a single `__init__.py`, no solver, no model. The
science lives in the two submodules below, each its own repository and its own
installable distribution.

```python
import lemaitre as lm

lm.initial_data.conformally_flat_puncture    # the Bowen–York puncture model — the paper package
lm.initial_data.curved_puncture              # its non-conformally-flat successor
```

Attribute access is lazy (PEP 562), and `pkgutil.extend_path` merges every
`lemaitre/initial_data/` directory on `sys.path`, so the models install and
import as siblings without either knowing where the other lives. Exactly one
installed distribution may own this namespace level, and that is this one.

## The two puncture models

### `conformally_flat_puncture` — [`LMID-conformally-flat-puncture`](LMID-conformally-flat-puncture)

Distribution `LMID-conformally-flat-puncture`. **The paper package** — code and
manuscript in one repository.

A certified, differentiable, parametric reduced-order model of the constraint
solve for quasi-circular **Bowen–York** punctures, up to the 8-D general-spin
model θ₈ = (b, q, χ_A, χ_B): a spectral xCFC solver on the Ansorg–Brügmann–Tichy
prolate chart, matrix-free Newton–Krylov, and a Smolyak/Hermite/POD
parameter-space ROM exposing `solve(θ, guess)` together with the tangent
`dU/dθ`. *Certified* has a precise meaning here — the solve interface returns a
datum only when its residual meets the gate, and reports the attempt as
uncertified otherwise, rather than returning an unqualified answer.

It accompanies *"A Differentiable Parametric Model of Binary-Black-Hole Initial
Data: I. Conformally flat Bowen–York punctures"* (De Ceuster & Li). The `I.` is
load-bearing: this is the first of a series, and `curved_puncture` below is the
second.

### `curved_puncture` — `LMID-curved-puncture`

Distribution `LMID-curved-puncture`. **In preparation — the repository is not
open yet.**

The non-conformally-flat successor: the same ABT chart, the same Newton–Krylov
solver and the same parametric layer, with the conformally flat background
replaced by a superposition of quasi-isotropic conformally-**Kerr** and
Lorentz-boosted-Schwarzschild 3-metrics. The motivation is spin: on conformally flat
Bowen–York data the dimensionless spin of a puncture **saturates at χ ≈ 0.93**
however large the free-data spin parameter is made — a limitation the first
paper states about itself.

The dependency runs one way: `curved_puncture` reuses `conformally_flat_puncture`
and so requires it; nothing in `conformally_flat_puncture` imports the successor.

> Because its repository is still closed, it is marked `update = none` in
> `.gitmodules`. A `git clone --recurse-submodules` therefore **succeeds** and
> leaves `LMID-curved-puncture/` empty, instead of aborting — which would
> otherwise take the rest of the tree down with it. If you have access, add it
> with `git submodule update --init --recursive --checkout`.

## Install

Both namespace parents — `lemaitre` and `LM-initial-data` — are published on
PyPI. The models are not, so install from a checkout of the family
superproject, **outermost first** and with `--no-deps`:

```bash
pip install numpy scipy jax matplotlib pytest sympy    # the solver stack + test deps

# from the Lemaitre superproject root — https://github.com/LemaitreModels/Lemaitre
for d in . LM-initial-data LM-initial-data/LMID-conformally-flat-puncture; do
  pip install -e "$d" --config-settings editable_mode=compat --no-deps
done

python -c "import lemaitre as lm; lm.initial_data.conformally_flat_puncture"   # smoke check
```

Add `LM-initial-data/LMID-curved-puncture` to that loop only if you have access
to it; the directory is empty otherwise.

Both flags are load-bearing, and for different reasons. **`--no-deps` and the
order** go together: without them pip resolves `lemaitre` and `LM-initial-data`
from PyPI in place of your checkout, and you end up testing a published parent
against a local child. **`editable_mode=compat`** is required because the modern
editable mode degrades the two namespace levels into PEP 420 portions, after
which lazy attribute access fails while a direct `import` still works — a
failure that looks like a bug in the model. See the leaf's `docs/STRUCTURE.md`.

This umbrella itself depends only on the `lemaitre` core and requires Python
≥ 3.10. The solver stack comes with whichever model you install; each model is
self-contained beyond it, enforced in the leaf by
`tests/test_self_containment.py`.

Each submodule builds, tests and releases on its own — see its own `README.md`
for the acceptance suite and, for `conformally_flat_puncture`, the
paper-reproduction targets.

## License

GPL-3.0 (see `LICENSE`).
