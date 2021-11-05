## Resources
- The delimiter/seperator used in all the files in this project is `<::>`. This is to avoid using common seperators like commas.
- The main file that is used to make decisions is `triggers.csv`. Avoid making too many trigger words. You can add as many comments as you like in the `{insert_trigger_type_here}.txt` files.

### Structure
- `triggers.csv`
    - Format: `trigger_types<::>re_triggers<::>priorities`
    1. `trigger_types` this column specifies the type of tigger words used in the sentence. Eg: `!Balayya` is classified as `salutation` type.
        - Each trigger_type has a seperate .txt file to choose replies from.
        - Eg: `drinking` trigger_type has a `drinking.txt` that contains replies such as 'sare, iroju Mansion House eddham mari'.
    2. `re_triggers` this column specifies the Regular Expression to match in the comment.
    3. `priorities` this column specifies the order in which the action specific to `trigger_type` is to be placed. lower is better.
        - Eg: `salutation` trigger_type has priority 1, so it is placed high in action queue. So, they are executed earlier compared to other trigger_types.
- `{trigger_type}.txt`
    - Format: each line has one comment.
    - Eg: drinking.txt, salutation.txt, mansion.txt, funny.txt, etc.
