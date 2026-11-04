# Analogy library

Tested anchor analogies for common kinds of AI-built work. Pick one anchor per explanation and map every major part onto it. Each set lists where the analogy breaks, so the explanation can say so.

## Contents
1. Web app or SaaS product
2. API and integrations
3. Data pipeline or analytics stack
4. Automation workflow (n8n, Zapier, Make, agents)
5. AI agent or chatbot system
6. Database design
7. Infrastructure and deployment
8. Contracts and legal terms
9. Policies and procedures
10. Marketing copy and content systems

---

## 1. Web app or SaaS product: a restaurant

| Part | Analogy | Breaks because |
|---|---|---|
| Front end (UI) | Dining room and menu | The dining room can be copied and changed by the guest (code runs in their browser) |
| Back end / server | Kitchen | One kitchen can serve thousands of tables at once |
| API | Waiter carrying orders | The waiter forgets you after each trip (stateless) |
| Database | Pantry and fridge | Nothing spoils, but nothing is thrown away unless someone decides to |
| Authentication | Host checking the reservation list | — |
| Authorization | Which rooms a guest may enter | — |
| Cache | Dishes kept warm under the heat lamp | Warm dishes can be out of date |
| Payments | Cashier using an outside card machine | The restaurant never holds the card itself (if done right) |
| Logs | Kitchen order tickets kept in a drawer | They can contain private details if careless |

## 2. API and integrations: a post office

- Request = a letter with an address and a clear form inside.
- Endpoint = a specific counter at the post office.
- API key = the signature that proves who sent the letter. If copied, anyone can send letters as you.
- Rate limit = the counter only accepts so many letters per hour.
- Webhook = the post office calls you when a parcel arrives instead of you checking every day.
- Breaks: letters arrive in milliseconds, and a lost letter is usually retried automatically.

## 3. Data pipeline or analytics stack: a water treatment system

- Sources = rivers and wells feeding in.
- Extraction = pumps pulling water in.
- Transformation and cleaning = filters and treatment tanks.
- Warehouse = the reservoir.
- Dashboards = taps in homes showing the result.
- Data quality checks = water testing labs.
- Breaks: data can be copied without being used up, and bad data looks just as clean as good data unless tested.

## 4. Automation workflow: a factory assembly line

- Trigger = the bell that starts the line (new email, form submitted, time of day).
- Nodes or steps = stations on the line, each doing one job.
- Conditions or branches = a sorter that sends items left or right.
- Credentials = keycards each station uses to open other buildings.
- Error handling = what happens when a station jams: stop the line, set the item aside, or keep going.
- Breaks: the line runs with nobody watching, so silent failures can go unnoticed for weeks.

## 5. AI agent or chatbot system: a new employee with a manual

- Model = the employee's general knowledge and skills.
- System prompt = the job description and rules given on day one.
- Tools = the systems the employee has logins for.
- Memory or retrieval = the filing cabinet they can look things up in.
- Guardrails = what the manager forbids, and who checks.
- Breaks: the employee is confident even when wrong, follows instructions hidden in documents they read, and forgets everything between shifts unless memory is built.

## 6. Database design: a library

- Tables = sections of the library (books, members, loans).
- Rows = individual cards in a section.
- Columns = fields on each card (title, author, year).
- Primary key = the unique barcode on each book.
- Foreign key = a loan card pointing to a member barcode and a book barcode.
- Index = the catalogue that makes finding things fast but takes space to maintain.
- Migration = reorganizing the shelves while the library stays open.
- Breaks: deleting a card can silently delete or orphan every card that points to it.

## 7. Infrastructure and deployment: renting space in a building

- Server or container = a rented office.
- Cloud provider = the building owner.
- Environment variables and secrets = the keys kept in a safe in the office.
- Deployment = moving furniture in.
- Scaling = renting more offices when the team grows, and paying for each one.
- Monitoring = security cameras and smoke detectors.
- Breaks: offices can be created and destroyed in seconds, and the bill can grow overnight without anyone moving in.

## 8. Contracts and legal terms: building a house together

- Scope of work = the architectural plans.
- Payment terms = the payment schedule tied to construction stages.
- Liability cap = the maximum the builder pays if something collapses.
- Indemnity = who pays the neighbour if the wall falls on their car.
- Termination = how either side can walk away halfway through, and who keeps what.
- Intellectual property = who owns the plans after the house is built.
- Governing law = which country's building code applies.
- Breaks: legal effect depends on jurisdiction. Always flag that a lawyer should confirm anything high-stakes.

## 9. Policies and procedures: airport security rules

- Policy = the posted rules.
- Procedure = the steps staff follow at the gate.
- Exceptions = who can approve skipping a step.
- Enforcement = what happens when someone breaks a rule.
- Breaks: an airport has staff checking every passenger, while a written policy only works if someone reads and follows it.

## 10. Marketing copy and content systems: a shop window

- Headline = the sign above the window.
- Value proposition = the main item on display.
- Proof (testimonials, data) = the reviews taped to the glass.
- Call to action = the open door.
- Tone of voice = how the shop is decorated and how staff speak.
- Claims = price tags. A wrong price tag can create legal problems.
- Breaks: the window is seen by people in many countries and cultures at once.
