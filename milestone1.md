# Milestone 1 — Pick a community and read it

**Community:** [r/Minecraft](https://www.reddit.com/r/Minecraft/)

**Research date:** October 20, 2026

**Status:** Community selected; AI-assisted research notes drafted. The student's twenty-minute reading and confirmation of the observations are still pending.

## Why this community

r/Minecraft is public and covers building, survival, game mechanics, updates, and different ways to play. This gives the project a topic the student chose and several kinds of text to compare. The community spans the game across many versions rather than concentrating on one new release.

The [public feed and community rules](https://www.reddit.com/r/Minecraft/) are visible without a login. Many submissions rely on pictures or videos, so the collection needs an explicit text-only scope.

## What counts as one post

- One example is a submission's title plus its written body, read together. Comments are not separate examples in this project.
- Include English-language discussions, opinions, suggestions, and questions whose meaning is clear from the text alone.
- A submission may have an attachment if its text still stands on its own. Exclude posts that require seeing a build, screenshot, video, or error image to understand them.
- Exclude bots, moderator announcements, advertisements, duplicate posts, and posts whose body has been removed or deleted.
- Keep Java/Bedrock and version details when the author supplies them. They can explain why apparently contradictory experiences differ.

The 35 entries below are an exploratory reading list, not the later 200-post training dataset. Before collecting that dataset, check that enough eligible posts are accessible and use a collection rule that does not select examples for the labels we hope to find.

## How these notes were made

Codex searched public r/Minecraft posts about survival, editions, updates, transportation, enchantments, inventory, and keep-inventory settings. It reviewed the titles and available body text before drafting the three distinctions below. The searches deliberately sought different topics; this is not a random or representative sample, and the proportions must not be treated as label frequencies.

Some individual pages were readable through the web tool; other links returned fetch errors, so their notes use publicly indexed post text. In the log, **Page** means the post body was available on an opened page; **Index** means the review relied on indexed text and needs verification at the link. An indexed copy may be incomplete or outdated. One known deleted post was excluded. These summaries describe what authors wrote, not independently verified facts about Minecraft.

This is an AI-assisted research draft, not a claim that the student personally read 35 posts or spent twenty minutes reading. During the student's reading, verify each entry, replace unavailable posts, and revise any observation that does not hold up. No training labels or unaided labeling have been recorded.

## Three candidate distinctions observed in the text

### 1. An opinion with an explicit reason versus an opinion stated alone

Some authors explain why a mechanic affects their experience; others give a preference without explaining it. The visible feature is a stated reason or consequence connected to the opinion. Length, a confident tone, and the words "hot take" do not settle this distinction.

- **Reason present:** [The elytra should not be nerfed](https://www.reddit.com/r/Minecraft/comments/1rigtgg/the_elytra_should_not_be_nerfed/) connects fast travel to the distances players need to cross.
- **Reason absent:** [What do you think is the BEST all-round enchantment?](https://www.reddit.com/r/Minecraft/comments/1oovo5g/what_do_you_think_is_the_best_allround_enchantment/) names Mending without explaining the preference.

**Boundary to investigate:** A named mechanic or a number is not automatically a reason. It needs to support the author's conclusion in the text. This distinction measures whether support is supplied, not whether the claim is true.

### 2. A concrete proposed change versus a general evaluation

Some posts describe a change to the game's behavior that a reader could explain back; others express satisfaction or dissatisfaction without specifying a change.

- **Concrete change:** [How would you "fix" the inventory problem?](https://www.reddit.com/r/Minecraft/comments/1ukeodx/how_would_you_fix_the_inventory_problem/) proposes a backpack that uses the chest equipment slot, creating a tradeoff with armor and elytra.
- **General evaluation:** [what do you guys think of the new update](https://www.reddit.com/r/Minecraft/comments/1e8zhi1) expresses approval without proposing a change.

**Boundary to investigate:** A suggestion can also contain an opinion and a reason. These features overlap; they are not yet mutually exclusive classifier labels. A vague wish for a better game needs a clearer proposed behavior to count as a concrete change.

### 3. A question with useful context or constraints versus a question missing them

Some questions give enough information to narrow an answer: edition, version, a specific symptom, attempted fixes, or restrictions on acceptable solutions. Others leave important details unstated. The relevant context depends on the question; a preference question does not need a hardware specification.

- **Useful constraints:** [Getting mending](https://www.reddit.com/r/Minecraft/comments/ih6xfk) supplies a server version and rules excluding villager trading and AFK fishing.
- **Troubleshooting detail:** [Help: Minecraft Java inventory drag bug?](https://www.reddit.com/r/Minecraft/comments/1sbbgmz/help_minecraft_java_inventory_drag_bug/) gives the mouse behavior, setup, and several settings already checked.
- **Missing setup:** [Keep inventory has been borked by the new easy mode game rule](https://www.reddit.com/r/Minecraft/comments/1hjv1iy) reports trouble but does not supply an edition, version, or reproducible sequence in the indexed text.

**Boundary to investigate:** Short questions can be precise. Count details that help answer the actual question, rather than counting words or treating every question as insubstantial.

## Reading log — 35 public submissions

The notes are paraphrases. Rows identify source posts, not assigned labels. Verify the original title and body rather than relying on these summaries during personal reading or later labeling.

| # | Source post | Access | Observation from the available text |
|---|---|---|---|
| 1 | [Slowing down Survival/Hardcore gameplay](https://www.reddit.com/r/Minecraft/comments/172k910) | Index | Asks how to stop rushing progression; names the desired experience but gives little about the current routine. |
| 2 | [Favorite exclusive mods from different sites](https://www.reddit.com/r/Minecraft/comments/1fqibf9) | Index | Requests recommendations and supplies mod sites, loaders, and examples of existing preferences. |
| 3 | [Help finding where to build](https://www.reddit.com/r/Minecraft/comments/178fup2) | Index | Describes repeatedly giving up while choosing a location; leaves desired terrain and building goals open. |
| 4 | [City logistics](https://www.reddit.com/r/Minecraft/comments/17612di) | Index | Defines a concrete problem: distribute food while keeping farms outside the villager city. |
| 5 | [Differences in modding capabilities between Java and Bedrock](https://www.reddit.com/r/Minecraft/comments/1duslmj) | Index | Narrows the comparison to what modifications can do and supplies an example modpack. |
| 6 | [Moving from Xbox to PC: Java or Bedrock?](https://www.reddit.com/r/Minecraft/comments/18dayzs) | Index | Requests an edition recommendation for a child and asks about difficulty joining custom servers. |
| 7 | [Hot take: update 1.21 sucks](https://www.reddit.com/r/Minecraft/comments/178kxz5) | Index | Strong criticism still names announced features and contrasts them with desired content. Tone alone would miss that support. |
| 8 | [What do you think of the new update?](https://www.reddit.com/r/Minecraft/comments/1e8zhi1) | Index | Gives a positive reaction without a feature, example, or reason. |
| 9 | [How to fix elytra](https://www.reddit.com/r/Minecraft/comments/1o56ml9) | Index | Proposes removing rocket boosting, names alternatives, and anticipates an objection. |
| 10 | [Elytra as end-game rather than mid-game content](https://www.reddit.com/r/Minecraft/comments/1g53qtg/hot_take_the_elytra_is_endgame_content_not_midgame/) | Page | Uses the author's slower playstyle to explain a disagreement about progression. |
| 11 | [The elytra should not be nerfed](https://www.reddit.com/r/Minecraft/comments/1rigtgg/the_elytra_should_not_be_nerfed/) | Page | Supports a position by describing the cost of crossing long distances. |
| 12 | [I adore the spear](https://www.reddit.com/r/Minecraft/comments/1q6ndzx/i_adore_the_spear/) | Page | Connects a movement mechanic to a preferred balance between speed and exploration. |
| 13 | [Elytra problem](https://www.reddit.com/r/Minecraft/comments/13b2uil) | Index | Seeks a datapack for a private server and specifies the kind of balance change wanted. |
| 14 | [Ideas for elytra-specific enchantments](https://www.reddit.com/r/Minecraft/comments/1hw9d48) | Index | Specifies separate enchantment effects and an acquisition idea rather than just asking for more content. |
| 15 | [Analyzing mace PvP](https://www.reddit.com/r/Minecraft/comments/1bgufk8) | Index | Lists combat interactions, counters, and possible effects on playstyles. |
| 16 | [Stop trying to make spears more expensive](https://www.reddit.com/r/Minecraft/comments/1ntxx70) | Index | Uses an angry tone but supplies an argument about mounts and confined spaces. |
| 17 | [Hear me out: balancing Mending](https://www.reddit.com/r/Minecraft/comments/1wrybq8/hear_me_out/) | Index | Describes repairing enchanted equipment with materials and explains the intended resource tradeoff. |
| 18 | [Unpopular Minecraft opinions and ideologies](https://www.reddit.com/r/Minecraft/comments/1l5w5y6) | Index | Explains opposition to Mending through a desired mining-and-building gameplay loop. |
| 19 | [Mending versus Unbreaking](https://www.reddit.com/r/Minecraft/comments/1fdwlef) | Index | A short question identifies a specific suspected redundancy between two enchantments. |
| 20 | [Getting Mending](https://www.reddit.com/r/Minecraft/comments/ih6xfk) | Index | Gives the version and server restrictions, making the recommendation request more constrained. |
| 21 | [Repair Netherite](https://www.reddit.com/r/Minecraft/comments/15g9jbd) | Index | Asks what to upgrade and which repair material is required; concrete questions in little text. |
| 22 | [Enchantments: a bow obtained through fishing](https://www.reddit.com/r/Minecraft/comments/1rsgjkf/enchantments/) | Page | Shares a personal result, enchantment details, and the process used to obtain them. |
| 23 | [Go-to spear enchantments](https://www.reddit.com/r/Minecraft/comments/1q9gpt8/what_are_your_goto_spear_enchantments/) | Page | Asks for preferences after briefly praising the enchantments; little supporting explanation. |
| 24 | [Inventory issue on an Android tablet](https://www.reddit.com/r/Minecraft/comments/1upnoql/inventory_issue_solution_tt/) | Page | Names the device, input method, and symptom, but does not list attempted fixes. |
| 25 | [How would you fix the inventory problem?](https://www.reddit.com/r/Minecraft/comments/1ukeodx/how_would_you_fix_the_inventory_problem/) | Page | Suggests storage changes with explicit equipment-slot tradeoffs and container restrictions. |
| 26 | [Java inventory drag bug](https://www.reddit.com/r/Minecraft/comments/1sbbgmz/help_minecraft_java_inventory_drag_bug/) | Page | Supplies the observed behavior, environment, and several checks already performed. |
| 27 | [Inventory not showing entities](https://www.reddit.com/r/Minecraft/comments/1subxuy/inventory_not_showing_entities/) | Page | Names the missing objects and later adds a resource-pack explanation; the edit changes the information available. |
| 28 | [Why does keep inventory require cheats?](https://www.reddit.com/r/Minecraft/comments/1tqzw5d/why_must_using_keep_inventory_require_using_cheats/) | Page | Identifies Bedrock and explains how losing items and disabling achievements affect enjoyment. |
| 29 | [Does anyone play with keep inventory on?](https://www.reddit.com/r/Minecraft/comments/1un2z4i/does_anyone_play_with_keep_inventory_on/) | Page | A brief preference and request for reassurance, with limited explanation of the actual gameplay experience. |
| 30 | [Keep inventory saved my love for the game](https://www.reddit.com/r/Minecraft/comments/1hpqvia/i_play_with_keep_inventory_on_and_it_has_saved_my/) | Page | Contrasts abandoning worlds after dying with continuing to explore after changing the setting. |
| 31 | [You can't cheat in Minecraft](https://www.reddit.com/r/Minecraft/comments/1uvs9v6/you_cant_cheat_in_minecraft/) | Page | Argues from sandbox freedom but qualifies the claim for multiplayer servers with agreed rules. |
| 32 | [Best all-round enchantment](https://www.reddit.com/r/Minecraft/comments/1oovo5g/what_do_you_think_is_the_best_allround_enchantment/) | Page | Names Mending as the author's choice without a reason; the title and caption stand alone. |
| 33 | [Improving the Keep Inventory command](https://www.reddit.com/r/Minecraft/comments/1cuwm1h) | Index | Proposes three specific alternatives involving slots, experience, or the cause of death. |
| 34 | [Keep inventory and the easy-mode rule](https://www.reddit.com/r/Minecraft/comments/1hjv1iy) | Index | Reports unexpected item loss but leaves edition, version, and reproduction details unstated. |
| 35 | [Keep inventory hate, I don't get it](https://www.reddit.com/r/Minecraft/comments/1usfru5/keep_inventory_hate_i_dont_get_it/) | Index | Connects the setting to relaxation and exploration while retaining other survival restrictions. |

## Before moving to Milestone 2

- [x] Select one public community: r/Minecraft.
- [x] Prepare a linked 35-post research log and three candidate distinctions with AI assistance.
- [ ] Spend about twenty minutes personally reading 30–40 eligible posts. Verify or replace entries above as needed.
- [ ] Confirm or revise the three distinctions using that reading, then commit the verified notes.

The final label taxonomy and five numerical acceptance criteria come in later milestones. These candidate distinctions describe observable features and can overlap.
