## Exercise 2: Review a completed form {#exercise-2-review-a-completed-form}

::: {.callout-note collapse="true" appearance="minimal" icon=false title="Open exercise"}

**Scenario:** A draft reimbursement claim needs a second check before submission. The draft deliberately contains several mistakes and missing details.

**Use:** [01_simulated_reimbursement_guide.md](materials/01_simulated_reimbursement_guide.md) **and** [02_simulated_completed_claim.md](materials/02_simulated_completed_claim.md).

**Try this prompt:**

```text
Review the attached completed claim against the attached reimbursement guide.

List possible mistakes or missing information in a table with: item, problem, relevant rule, and suggested next step. Check the calculations. Separate clear errors from points that need clarification. Do not assume that missing approvals exist or that the claim has been approved.
```

**Then try:** Ask which entries follow the guide, not just which ones have problems.

**Check:** Did it find the deliberate mistakes without adding rules that are not in the guide? Did it separate clear mistakes from questions that need clarification? Review the findings before changing or submitting the claim.

<details>
<summary>What to look for (after trying)</summary>

For example, the cost centre is blank, and the expenses add up to €262.60, not €263.60. Check the rules for approvals, receipts and deadlines too.

</details>

**Want to reuse this?** Try [Exercise 12](#exercise-12-build-a-reusable-form-reviewer-persona) to configure a form-reviewing Persona and test it on a different claim.

:::
