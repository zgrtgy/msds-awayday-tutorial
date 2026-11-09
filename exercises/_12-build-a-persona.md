## Exercise 12: Build a reusable form-reviewer Persona {#exercise-12-build-a-reusable-form-reviewer-persona}

::: {.callout-note collapse="true" appearance="minimal" icon=false title="Open exercise"}

**Scenario.** Checking forms against a procedure is recurring work. A Persona can keep your checking method consistent when a new form arrives.

**Use:** [01_simulated_reimbursement_guide.md](materials/01_simulated_reimbursement_guide.md), [02_simulated_completed_claim.md](materials/02_simulated_completed_claim.md), and [09_simulated_second_claim.md](materials/09_simulated_second_claim.md).

1. If you have not done Exercise 2, first attach the guide and first claim to a normal chat and request a check using the Exercise 2 prompt.
2. Open **Personas** and create a Persona named *Expense claim reviewer*. Give it the instructions below. If the Persona editor supports **Sources/reference documents**, attach the fictional reimbursement guide there. Otherwise attach the guide whenever you use the Persona.
3. Open a **new chat using the Persona** and attach [09_simulated_second_claim.md](materials/09_simulated_second_claim.md) (and the guide if it is not attached to the Persona).
4. Ask: *Review this draft claim against the reimbursement guide. What requires attention, and what appears compliant?*

**Persona instructions** (save these as the Persona's working method, not as a one-time chat message):

```text
You help staff review draft expense claims against a supplied procedure.

Check required fields, supporting receipts, approvals, deadlines, expense limits and arithmetic. For possible problems, cite the relevant rule and the form entry. Separate confirmed mismatches from missing documentation or uncertainty.

Use only the supplied guide as the authority. Do not invent requirements, approve claims or submit anything. End with a short list of issues for a person to review.
```

**Check:** Does the Persona identify the *new* claim's issues without carrying over problems unique to the first claim? Can it show which rules support its findings? Would a saved Prompt have been sufficient for this task, or did the Persona make recurring review easier?

*If source attachment or Persona settings differ in UU AI-Chat, keep the instructions in the Persona and attach the guide within the chat. The benefit being tested is reusable behaviour—not a particular settings panel.*

:::
