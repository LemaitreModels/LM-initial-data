"""``lemaitre.initial_data`` — namespace level for the initial-data models.

The **umbrella** of the initial-data domain.  Like :mod:`lemaitre` itself this
ships no science: it owns this one ``__init__.py`` so that the individual
initial-data models can live in their own repositories and distributions while
importing as siblings::

    import lemaitre as lm

    lm.initial_data.conformally_flat_puncture    # LMID-conformally-flat-puncture
    lm.initial_data.curved_puncture              # LMID-curved-puncture

===================================================  ==================================
namespace                                            distribution / repository
===================================================  ==================================
``lemaitre.initial_data``                            ``LM-initial-data`` (this file)
``lemaitre.initial_data.conformally_flat_puncture``  ``LMID-conformally-flat-puncture``
``lemaitre.initial_data.curved_puncture``            ``LMID-curved-puncture``
===================================================  ==================================

Every distribution carries the name of its repository.

**conformally_flat_puncture** is the published model: certified, differentiable,
parametric Bowen–York puncture data on the Ansorg–Brügmann–Tichy chart, with the
paper.  **curved_puncture** is its non-conformally-flat successor — the same chart and
solver, a superposed quasi-isotropic-Kerr / boosted-Schwarzschild background —
which reaches the spins conformal flatness cannot represent at all.

This is the *second* namespace level, and it works exactly like the root:
``pkgutil.extend_path`` merges every ``lemaitre/initial_data/`` directory on
``sys.path``, and a PEP 562 ``__getattr__`` imports the model packages lazily on
attribute access.

Family bookkeeping: exactly ONE installed distribution may own this
``lemaitre/initial_data/__init__.py``, and that is ``LM-initial-data``.
The model leaves ship only their own leaf package — never this file, and never
``lemaitre/__init__.py`` (which belongs to the ``lemaitre`` core).
"""
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

__version__ = "0.1.0"


def __getattr__(name):
    import importlib

    try:
        return importlib.import_module(f"{__name__}.{name}")
    except ModuleNotFoundError as exc:
        raise AttributeError(
            f"module {__name__!r} has no attribute {name!r} "
            f"(no installed 'lemaitre.initial_data.{name}' model package)"
        ) from exc
