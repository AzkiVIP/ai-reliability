# Compatibility and platform notes

## Portable format, host-dependent loading

This package uses the Agent Skills-style structure: one directory, a required `SKILL.md` with YAML frontmatter (`name`, `description`), and optional supporting Markdown references. This structure is documented by OpenAI and Anthropic, and the open Agent Skills format is used by multiple agent environments.

However, **file format compatibility is not identical to runtime compatibility**. A host must be able to discover the skill directory and read sibling files for on-demand module loading to work.

## Host capability checklist

Before claiming that the skill works in a target AI product, verify:

- [ ] It accepts a folder/bundle containing `SKILL.md`.
- [ ] It reads the `name` and `description` frontmatter correctly.
- [ ] It makes the skill discoverable at the intended time.
- [ ] The model can read `references/*.md` when the main file points to them.
- [ ] The host preserves relative file paths after installation or upload.
- [ ] The model can follow the router without loading every module.
- [ ] The host's system/developer policies and tool rules remain higher priority.
- [ ] The model has been evaluated on representative tasks.

## Known ecosystem notes (check current docs before deployment)

- **OpenAI API / Codex environments:** official documentation describes skills as folders with a required `SKILL.md` and optional supporting files. Available skill directories are surfaced to the model, which can read the manifest and supporting files in its execution environment. Codex also documents repository/user skill locations. Exact setup depends on product and runtime.
- **Anthropic Claude environments:** official documentation describes filesystem-based skills and progressive disclosure. The runtime reads `SKILL.md` when a skill is invoked and can read linked reference files as needed. Availability differs by product and deployment.
- **Other AI products:** do not assume support based on Markdown alone. Confirm whether they support the Agent Skills format, filesystem access, relative references, and dynamic loading. If not, use a platform-specific adapter or manually include only the needed module.

## Fallback when modules cannot be loaded

1. Use the universal rules in `SKILL.md`.
2. Identify the task type using the module router.
3. If the user or host can provide files, read only the one or two references required.
4. Otherwise, apply the core principles without claiming that a specialist reference was loaded.
5. If the missing module would materially change the quality or safety of the result, disclose the limitation or request the file.

## Token-cost note

Bundled files do not necessarily cost tokens merely because they exist in a directory. They do cost context when the host or model reads/inserts them. Different hosts may preload metadata, full instructions, or selected references differently. Measure actual behaviour rather than promising zero token cost.

## Official documentation

- OpenAI Skills: https://developers.openai.com/api/docs/guides/tools-skills
- OpenAI skill creator (source): https://github.com/openai/skills/tree/main/skills/.system/skill-creator
- ChatGPT Learn — Build skills: https://learn.chatgpt.com/docs/build-skills
- Anthropic Agent Skills overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Agent Skills specification: https://agentskills.io/specification
