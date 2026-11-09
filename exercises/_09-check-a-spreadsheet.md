## Exercise 9: Check a simple spreadsheet {#exercise-9-check-a-simple-spreadsheet}

::: {.callout-note collapse="true" appearance="minimal" icon=false title="Open exercise"}

**Scenario:** You have a small list of purchases for an event and want to check the calculations.

**Use:** [08_simulated_purchases.csv](materials/08_simulated_purchases.csv).

**Try this prompt:**

```text
Check the attached purchase list. For each row, compare quantity × unit price with the reported total.

List incorrect totals in a small table, show the correct calculations, and explain how I could do this check with an Excel formula. Do not silently correct the source data. Summarise the total difference, if any.
```

**Then try:** Ask which items contribute most to the total estimated cost, or ask for a formula to calculate the total by category.

**Check:** Did it identify the correct rows and calculate accurately? Can you verify a couple of items yourself with a calculator?

<details>
<summary>What to look for (after trying)</summary>

The marker packs should cost €14.50, not €12.50. The notepads should cost €36.00, not €35.00.

</details>

:::
