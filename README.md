# Xunpu AI Synth 0.4 · Portfolio Preview

Explainable Text-to-Timbre design for a native macOS AU, VST3 and Standalone instrument.

This is a **selective portfolio preview**, not the complete product or a deployable service.
It contains public architecture notes, a small offline interface example, and selected evidence.
Production analysis algorithms, prompts, model weights, server routes, credentials, service URLs,
customer records, and private datasets are not included. Examples explicitly marked synthetic are
illustrations, not experimental predictions. No remote API is called by these examples.


## Architecture

Natural-language brief → private model adapter → validated patch contract → local C++ DSP
→ playable audio → parameter refinement / A–B comparison / saved patch / WAV export.

The 0.4 synthesis-only MVP starts from init, exposes 90 host parameters and has a 16-voice engine.
The model plans parameters; the local engine computes audio. This is not remote text-to-audio
generation. The earlier 0.3 sample-based instrument remains a distinct historical target.

## Selected recorded checks

- Apple strict AU validation and a JUCE VST3 host harness passed in the recorded arm64 build.
- Five real provider-designed families produced finite, nonzero local WAV renders.
- Seventeen parameter-sensitivity measurements and eight modulation-route checks are recorded.
- A one-field UI refinement changed cutoff 1500 → 1800 Hz while preserving the other 89 parameters.
- Offline replay of a saved design matched the prior render in the recorded case.

Conditions: Apple M4, macOS 27.0.1; principally 48 kHz stereo, 128-frame blocks.
Core fixtures: C4, velocity 0.8, 1 s hold / 3 s total. Provider/export previews: 2 s hold / 8 s total.
These are historical engineering checks from 21 October 2026, not new checks performed by this preview.
No arbitrary-prompt success rate, perceptual sound-quality score, named DAW session, physical MIDI
validation, commercial-grade readiness, or universal CPU guarantee is claimed.

## Small public code sample

`python3 examples/patch_summary.py` reads a synthetic patch summary and validates two illustrative
fields. It contains no actual DSP engine, private patch schema, model prompts or transport adapter.

[Website / listen to real recordings](https://daixudong.art/synth.html) · [Attribution](ATTRIBUTION.md)
