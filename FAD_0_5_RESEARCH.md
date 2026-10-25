# FAD 0.5 · recorded local research evidence

Source revision: `f5260d8612a1533dfe6d2aeba2ab22a08880faa7` on the independent `feat/fad-engine-research` branch.

The model plans editable parameters. Audio is computed by the actual third-party local FAD render engine through the Xunpu adapter. The UI/audio snapshot boundary, network worker and dedicated effect-graph worker are separate.

## Recorded conditions

The supplied engineering records use fixed seeds and controlled MIDI fixtures. Parameter sensitivity means a measured difference between controlled render conditions. It is not a listening score or a claim that an arbitrary prompt succeeds.

The native host exposes 559 fields. Eight LFOs and 32 matrix rows are reachable through grouped UI controls. Ten effect slots can select thirteen effect types. Init/Generate, sparse Refine, A/B, state serialization and the fixed C4 8-second stereo export were checked locally. Live provider planning was recorded separately from the five code-authored engineering fixtures.

## Limits

- The combined application remains local private research; no combined installer or source distribution is published here.
- No audio-to-synthesis inversion, true text-to-audio generation, external sample import, formal perceptual study or named DAW-session validation is claimed.
- The callback C++ allocation instrumentation is workload-specific and is not a complete C-allocation or OS scheduling audit.
- The export preview can truncate long tails; performance recording should use a DAW.
- 0.5 patches use a distinct contract and are not presented as interchangeable with 0.4 patches.

The public JSON is copied from the supplied local validation result and contains only aggregate booleans, counts and render-difference measurements. It contains no provider credentials, prompts, customer data or deployable transport implementation.
