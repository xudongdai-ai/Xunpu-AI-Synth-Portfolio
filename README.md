# Xunpu AI Synth · Public Research Portfolio

Explainable Text-to-Timbre design for a native macOS AU, VST3 and Standalone instrument.

This is a **selective portfolio preview**, not the complete product or a deployable service.
It contains public architecture notes, a small offline interface example, and selected evidence.
Production analysis algorithms, prompts, model weights, server routes, credentials, service URLs,
customer records, and private datasets are not included. Examples explicitly marked synthetic are
illustrations, not experimental predictions. No remote API is called by these examples.



## 0.5 local research update · 25 October 2026

An independent **local research build** now integrates third-party FAD Core through the Xunpu adapter. The original 0.4 remains available separately. This update publishes architecture and selected engineering measurements, not the combined application, FAD source, private model adapter or deployable service.

- 559 canonical host/state fields; 16 voices; MPE bend, legato and glide checks.
- Eight LFOs, 32 modulation rows, ten effect slots and thirteen effect types.
- Waveform / wavetable position / warp / FM / cross-modulation / sub / noise / envelope and effect sensitivity measurements produced nonzero differences in the recorded fixtures.
- A/B and state restore, deterministic seed replay, fixed 8-second WAV preview export, and continued audio/effect preparation during delayed HTTP were checked.
- The instrumented C++ callback observed zero new/delete allocations in the recorded workload. This does not establish a universal real-time or operating-system scheduling guarantee.
- Real provider planning and refinement records changed 78, 18, and then one parameter; the one-field test changed only the requested field.
- The recorded local AU strict validation and JUCE VST3 host check passed. Named DAW projects, physical MIDI, formal listening evaluation and extended CPU/aliasing stress tests remain outstanding.

See [research scope and conditions](FAD_0_5_RESEARCH.md), [measured sensitivity records](fad_0_5_measurements.json), and [thread/engine architecture](fad_0_5_architecture.svg).

### Product film

[Watch / download the 85-second horizontal product film](promo_horizontal_v2.mp4).
This is the 24 October product/concept film using the earlier interface and supplied audio. It is **not** a recording of the new FAD 0.5 research build and does not demonstrate unimplemented audio inversion or text-to-audio capabilities.

### Attribution and distribution scope

FAD Core is third-party work from [willren5/FAD_Engine](https://github.com/willren5/FAD_Engine), under its custom openFAD 0.1 terms. Compatibility permission for public distribution of the combined JUCE/AGPL/openFAD application has not been established. No combined binary or upstream source is distributed in this update. The existing product licences and attributions remain in force.

## Historical 0.4 architecture

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
