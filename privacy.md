---
title: Privacy Policy
layout: default
---

# Privacy Policy
**Budgie**
_Last updated: 5 September 2026_

---

## 1. Introduction
This Privacy Policy explains how **Budgie** (“the App”, “we”, “us”) collects, uses, stores, and protects your information.

Budgie is available in multiple countries, and we are committed to protecting your privacy regardless of where you live. Depending on your location, different privacy laws may apply to you, and you may have additional rights under your local law (see Section 7).

Budgie is a personal budgeting app. By default your budgeting data is kept **locally on your device**, but the App also offers optional features — signing in, cloud sync, **AI‑generated insights**, and a paid **Budgie Pro** subscription — that involve sending or storing data on third‑party servers, and it displays advertising. This policy describes all of those cases. By using the App, you agree to this policy.

---

## 2. Information We Collect

### 2.1 Account & Profile Data
Budgie does **not** require an account to use its core budgeting features. If you choose to sign in (to enable cloud sync), you authenticate through **Apple** or **Google**. In that case we receive a basic account identifier and an email address (which may be Apple’s private relay address if you choose to hide your email). We do **not** create, see, or store any password.

### 2.2 Budgeting Data
Data you enter into the App, which may include:
- Expense and income entries (amounts, dates, categories, and optional notes)
- Budgets and savings goals
- Recurring income and expense series
- Custom categories
- App preferences and settings (e.g. currency)

This data is stored **locally on your device** by default. It is only transmitted off your device if you enable cloud sync (see 2.3), turn on AI insights (see 2.7), or use the export/backup feature.

### 2.3 Cloud Sync Data (Budgie Pro)
Cloud sync is **off by default** and requires an active **Budgie Pro** subscription (see 2.6). If you sign in, subscribe to Budgie Pro, and turn on **“Sync to cloud,”** your budgeting data (entries, budgets, recurring series, custom categories, and settings) is stored in **Google Firebase Firestore** under your account so it can sync across your devices. You can turn sync off at any time in Settings, and sync stops automatically if your subscription lapses.

### 2.4 Advertising Data
The App displays advertisements served by **Google AdMob**. To deliver and measure ads, Google may collect device identifiers, IP address, and usage data. On iOS, the App uses **App Tracking Transparency** to ask your permission before any tracking that requires it. Users in the EEA and UK are shown a **consent form** (via Google’s User Messaging Platform) and can choose personalized or non‑personalized ads. Advertising is **removed entirely for Budgie Pro subscribers** (see 2.6).

### 2.5 Automatically Collected Data
When you use cloud sync or see ads, standard technical information (such as device type, operating system, and IP address) may be processed by the relevant third‑party service to operate that feature securely.

### 2.6 Subscription & Purchase Data (Budgie Pro)
Budgie Pro is an optional paid subscription that unlocks cloud sync and an ad‑free experience. Purchases and subscriptions are processed through the **Apple App Store** or **Google Play** and managed with **RevenueCat**. To validate your purchase and keep your Pro access up to date, RevenueCat processes information provided by Apple or Google such as your **transaction receipt**, an **app‑user identifier** (linked to your Budgie account), your **device identifier**, and your **region/store country**.

We do **not** receive or store your full payment details, such as credit card numbers — all billing is handled by Apple or Google. RevenueCat only stores the information needed to confirm your purchase and maintain your entitlements. You can learn more in RevenueCat's [Privacy Policy](https://www.revenuecat.com/privacy/).

We do **not** collect or store your bank account or payment card details, and Budgie does not connect to your financial institutions.

### 2.7 AI Insights Data (OpenAI)
Budgie can generate short "insight cards" about your spending — a surprising total, a change since last month, a suggestion tied to one of your goals. Writing those cards requires sending a summary of your finances to **OpenAI**, which acts as a processor on our behalf.

**This feature is off by default.** It is a per‑device opt‑in: nothing is sent to OpenAI unless you turn on **Profile → AI insights → Write insights**, and it also requires that you are signed in. Insights are available to all users — free users unlock each card by watching a rewarded ad, and Budgie Pro subscribers get a higher daily allowance without ads (see 2.6).

**What is sent.** When you generate insights, the App builds a summary on your device and sends it, via our own secure server function, to OpenAI. That summary contains **aggregated figures covering roughly the last six months**:

- your currency and the date the summary was built
- your net worth figure and recent monthly saving rate
- monthly totals — income, spending, and the difference — per month
- per‑category totals, the number of entries in each, and monthly averages
- percentage changes in category spending between periods
- your savings goals, including the **name you gave each goal**, its target amount, target month, and progress
- your budgets, including the **name of each budget**, its limit, and how much is tracked against it
- your recurring commitments — the **category name**, amount, and frequency of each

Because goal names, budget names, and any custom category names you create are your own words, please keep in mind that whatever you type into those fields forms part of what is sent.

**What is never sent.** Your **entry notes**, your **individual transactions**, and the dates and details of any single purchase never leave your device. Neither does your name, email address, account identifier, device identifier, or location — OpenAI receives the financial summary only, with nothing identifying you attached to it.

**How OpenAI handles it.** We use OpenAI's business API. Under OpenAI's platform policy, data submitted through the API is **not used to train their models**, and is retained by OpenAI for a limited period (currently up to 30 days) for abuse monitoring before deletion. OpenAI's own handling is governed by their [Privacy Policy](https://openai.com/policies/privacy-policy) and [API data usage policies](https://openai.com/policies/api-data-usage-policies). Processing takes place on OpenAI's servers, which are located in the **United States** (see Section 10).

**What we store.** The cards that come back are stored **on your device only** — we do not keep a copy, and they are not written to cloud sync. On our servers we keep a simple **daily counter** of how many times you have generated insights (a date and a number, linked to your account), purely to enforce fair‑use limits and control costs. That counter contains none of your financial data. Our server logs may record an account identifier and technical error details when a generation fails, so that we can diagnose problems.

**Your control.** You can turn insights off at any time in **Profile → AI insights**. Turning the switch off **deletes the cards already generated on your device** and stops anything further being sent. Deleting your account (Section 8) also removes the usage counter described above.

---

## 3. How We Use Information
We use the information described above solely to:
- Provide the App’s budgeting features and display your data
- Authenticate you when you sign in
- Sync your data across your devices when you enable cloud sync
- Generate AI insight cards, when you have turned that feature on
- Display and measure advertising
- Maintain the security and reliability of the App
- Enforce fair‑use limits on features that cost us money to run
- Comply with our legal obligations

All budgeting calculations and charts are produced **on your device**. The only feature that sends your budgeting information off your device for processing is **AI insights**, and only if you opt in (see 2.7).

---

## 4. Third‑Party Services
Budgie relies on the following third‑party services, each governed by its own privacy policy:

| Service | Purpose |
| --- | --- |
| **Firebase Authentication** | User sign‑in (via Apple or Google) |
| **Firebase Firestore** | Optional cloud data storage and sync |
| **Firebase Cloud Functions** | Our own server function, which relays AI insight requests |
| **OpenAI** | Generating AI insight cards from an aggregated summary (opt‑in) |
| **Google AdMob** | Advertising |
| **Google User Messaging Platform (UMP)** | Ad consent management |
| **Sign in with Apple / Google Sign‑In** | Account authentication |
| **RevenueCat** | Subscription validation and entitlements |
| **Apple App Store / Google Play** | Subscription billing and payments |

Google’s handling of data is governed by the [Google Privacy Policy](https://policies.google.com/privacy). Apple’s handling of Sign in with Apple is governed by the [Apple Privacy Policy](https://www.apple.com/legal/privacy/). OpenAI’s handling of data sent for AI insights is governed by the [OpenAI Privacy Policy](https://openai.com/policies/privacy-policy).

We do **not** sell your personal or financial data for money, and we do **not** allow any third party to use your budgeting data to train AI models. However, when personalized advertising is enabled, our advertising partners may receive advertising identifiers and app usage data. Under some US state privacy laws — including the CCPA/CPRA in California — this kind of cross‑context behavioural advertising is treated as a “sale” or “sharing” of personal information. You can opt out at any time; see Section 5.

---

## 5. Advertising & Your Choices
You can manage how ads are personalized:
- On **iOS**, you can change tracking permission in your device’s Settings, and review your choices via **Settings → Privacy options** in the App (where available).
- On **Android**, you can reset or limit your advertising ID in your device settings.
- In the EEA/UK, you can re‑open the consent form at any time via **Settings → Privacy options**.

If you are a US resident, you can opt out of the sale or sharing of your personal information for cross‑context behavioural advertising at any time via **Settings → Privacy options** in the App. Opting out does not remove ads; it means the ads you see are not personalized. You can remove ads entirely by subscribing to **Budgie Pro**.

---

## 6. Your Privacy Rights
Depending on where you live, you may have some or all of the following rights in relation to the personal information we hold about you:
- **Access** the personal information we hold about you
- **Correct** inaccurate or incomplete information
- **Delete** your account and associated data
- **Opt out** of personalized advertising
- **Opt out** of AI insights, by turning the feature off in **Profile → AI insights**
- **Withdraw consent** where our processing relies on your consent
- **Receive a copy** of the data you provided to us in a portable format — you can export it yourself at any time via **Settings → Export**
- **Restrict or object to** certain processing, where your local law provides for it
- **Lodge a complaint** with your local privacy regulator

To exercise any of these rights, use the in‑app controls (for example **Settings → Delete account**) or contact us (see Section 12). Some rights, and the way they apply, depend on the privacy laws of your country — see Section 7.

---

## 7. Applicable Privacy Laws
Budgie is offered internationally. The privacy laws that apply to you depend on where you live.

### Australia
We handle your information in accordance with the **Australian Privacy Act 1988** and the **Australian Privacy Principles (APPs)**. If you are in Australia and have a privacy complaint, you may contact us (see Section 12) and, if unsatisfied, lodge a complaint with the **Office of the Australian Information Commissioner (OAIC)** at [oaic.gov.au](https://www.oaic.gov.au).

### Canada
We handle your information in accordance with the **Personal Information Protection and Electronic Documents Act (PIPEDA)**. If you are in Canada and have a privacy complaint, you may contact our Privacy Officer (see Section 12) and, if unsatisfied, lodge a complaint with the **Office of the Privacy Commissioner of Canada (OPC)** at [priv.gc.ca](https://priv.gc.ca).

If you live in Quebec, you also have rights under the **Act respecting the protection of personal information in the private sector** (“Law 25”). These include the rights to be informed about, access, correct and delete your information, to withdraw your consent, and to receive a copy of the information you provided to us in a structured, commonly used technological format — you can export your data yourself at any time via **Settings → Export** in the App.

Budgie shows advertising that uses profiling. You can deactivate this at any time by declining tracking when prompted on iOS, or by turning tracking off for Budgie in your device’s Settings at any time afterwards. Section 5 describes these choices in more detail.

Quebec complaints may be directed to the **Commission d’accès à l’information du Québec (CAI)** at [cai.gouv.qc.ca](https://cai.gouv.qc.ca).

### European Economic Area & United Kingdom
If you are in the EEA or the UK, we process your personal data in accordance with the **EU General Data Protection Regulation (GDPR)** and, in the UK, the **UK GDPR** and the **Data Protection Act 2018**.

**Controller.** The controller of your personal data is **Etienne Petrel**, Sydney NSW 2000, Australia, the developer of Budgie, contactable at support@tap-app.com.au (see Section 12).

**Representative in the EU and UK.** ⚠️ **DO NOT MERGE WITH THIS PLACEHOLDER.** Budgie is operated from outside the EEA and the UK, so Article 27 requires a designated representative in each unless an exemption applies. Replace this paragraph with the representative’s name and contact address, or with the reasoned basis for relying on the Art. 27(2) exemption, before this page goes live.

**Legal bases.** We rely on the following legal bases under Article 6(1):

| What we process | Why | Legal basis |
| --- | --- | --- |
| Account and profile data (2.1) | To create and authenticate your account | **Contract** — Art. 6(1)(b) |
| Budgeting data held in cloud sync (2.3) | To provide cloud sync to Budgie Pro subscribers | **Contract** — Art. 6(1)(b) |
| Subscription and purchase data (2.6) | To validate and manage your Budgie Pro subscription | **Contract** — Art. 6(1)(b) |
| The aggregated summary sent for AI insights (2.7) | To generate insight cards | **Consent** — Art. 6(1)(a) |
| Advertising identifiers and ad usage data (2.4) | To display and measure advertising | **Consent** — Art. 6(1)(a), gathered through the consent form described in Section 5 |
| Automatically collected diagnostic data (2.5), abuse prevention and fair‑use limits | To keep the App secure and reliable, and to limit features that cost us money to run | **Legitimate interests** — Art. 6(1)(f) |
| Records we are required to keep | To comply with our legal obligations | **Legal obligation** — Art. 6(1)(c) |

Where we rely on **consent**, you can withdraw it at any time — through **Settings → Privacy options** for advertising, and **Profile → AI insights** for AI insights — without affecting the lawfulness of processing carried out before you withdrew it. Where we rely on **legitimate interests**, you can object at any time (see below).

Budgeting data that never leaves your device is not processed by us at all.

**Your rights.** In addition to the rights listed in Section 6, you have the right to:
- **Restrict** our processing of your personal data in certain circumstances (Art. 18)
- **Object** to processing based on our legitimate interests (Art. 21), and to object at any time to processing for direct marketing, including the ad profiling described in Section 5
- **Data portability** — receive the personal data you provided to us in a structured, commonly used, machine‑readable format (Art. 20). You can export your budgeting data yourself at any time via **Settings → Export** in the App.
- **Not be subject to a decision based solely on automated processing** that produces legal or similarly significant effects (Art. 22). We make no such decisions. AI insight cards are informational suggestions only; they do not decide anything about you, and nothing in the App changes based on them.

We do not charge for exercising these rights, and we will respond within one month, as required by Art. 12(3).

**Complaints.** You may lodge a complaint with the supervisory authority in the EEA member state where you live, work, or where you believe an infringement occurred — the full list is published by the [European Data Protection Board](https://www.edpb.europa.eu/about-edpb/about-edpb/members_en). In the UK, the supervisory authority is the [Information Commissioner’s Office (ICO)](https://ico.org.uk). We would appreciate the chance to address your concern first (see Section 12), but you are not required to contact us before complaining.

**International transfers.** Your data is stored and processed outside the EEA and the UK — see Section 10, which describes where, and the transfer safeguards we rely on.

### United States (including California)
Depending on your state of residence, you may have rights under state privacy laws such as the **California Consumer Privacy Act (CCPA/CPRA)** and comparable laws in other US states. These may include the right to know what personal information we process, to request a copy of it, to correct it, to request its deletion, and to opt out of the sale or sharing of your personal information for targeted or cross‑context behavioural advertising.

We do **not** sell your personal information for money. As explained in Section 4, personalized advertising may nonetheless constitute a “sale” or “sharing” under these laws. To opt out, use **Settings → Privacy options** in the App, or decline tracking when prompted on iOS. You can also limit ad personalization using the other choices described in Section 5.

To exercise access, correction or deletion rights, contact us (see Section 12). You can also delete your account and its synced data yourself at any time via **Settings → Delete account** in the App. We will not discriminate against you for exercising any of these rights.

### Other countries
Many countries have their own privacy laws, most of which provide rights similar to those in Section 6. Where such laws apply to you, we will honour the rights they grant. If you have questions about your rights, or wish to reach the privacy regulator in your country, please contact us (see Section 12).

---

## 8. Data Retention & Deletion
- **Local data** remains on your device until you delete it within the App or uninstall the App. Uninstalling removes all locally stored data.
- **Cloud sync data** is stored until you delete it. You can permanently delete your account and all associated cloud data at any time via **Settings → Delete account**, which removes your Firebase authentication record and your Firestore data.
- **AI insight cards** are held on your device only, and are refreshed or replaced as your data changes. They are deleted when you turn off **Profile → AI insights**, when you erase your data, or when you delete your account. The summary sent to OpenAI is retained by OpenAI for a limited period (currently up to 30 days) for abuse monitoring and then deleted, under their API policy; the daily usage counter we keep is removed when you delete your account.
- **Subscription and purchase records** held by RevenueCat and the app stores are retained under their respective policies. You manage or cancel a Budgie Pro subscription through your Apple App Store or Google Play account.
- Alternatively, you can request deletion by emailing us (see Section 12).

---

## 9. Children’s Privacy
Budgie is not directed at children under the age of 13, and we do not knowingly collect personal information from children. If you believe a child has provided us with personal information, please contact us so we can delete it.

This age refers to the collection of personal information and is separate from the minimum age to accept our [Terms of Use](./terms.md) and from the age‑suitability rating shown for the App on the Apple App Store and Google Play.

If you are in the EEA or the UK, the age at which you can consent to the processing described in this policy on your own — the “digital consent age” under Article 8 of the GDPR — is **16**, unless the country you live in has set a lower age (member states may set it as low as 13). Below that age, the features that rely on consent — personalized advertising and AI insights — require the consent of a parent or guardian. Our [Terms of Use](./terms.md) separately require you to be at least 16, or to have a parent or guardian’s permission, to use the App at all.

---

## 10. Data Security & International Transfers
Data handled through **Google Firebase / Firestore** is **encrypted in transit** (using TLS) and **encrypted at rest** on Google’s servers, using the security measures provided by Google. This is standard server‑side encryption; it is **not** end‑to‑end encryption, which means the providers that operate these services are technically able to access the data in order to run them. On your device, budgeting data is protected by your device’s standard operating‑system protections.

Summaries sent for **AI insights** travel over an encrypted (TLS) connection to our server function and on to OpenAI, and are processed on OpenAI's servers in the **United States**.

Because Google, Apple, OpenAI, and our other providers operate globally, your information may be stored or processed on servers located **outside your country**, including in countries whose data‑protection laws differ from your own. Specifically, cloud sync data is stored in **Google’s United States multi‑region**, and both our own server function and OpenAI’s processing of AI insight summaries take place in the **United States**.

**Transfers out of the EEA and the UK.** Where we transfer personal data out of the EEA or the UK, we rely on the European Commission’s (and, for the UK, the ICO’s) **Standard Contractual Clauses**, incorporated into our agreements with the providers listed in Section 4, and — where the provider is certified — on the **EU–US Data Privacy Framework** and its UK extension. You can request a copy of the safeguards that apply to a particular transfer by contacting us (see Section 12). We use established, widely‑used providers and take reasonable steps to protect your information. However, no method of transmission or storage is completely secure, and we cannot guarantee absolute security.

---

## 11. Updates to This Policy
This Privacy Policy may be updated periodically. Any changes take effect once posted within the App or on this page. The “Last updated” date above reflects the latest revision.

---

## 12. Contact
If you have questions about this Privacy Policy or wish to exercise your privacy rights, please contact us:

📧 **support@tap-app.com.au**

📮 **Etienne Petrel**  
Sydney NSW 2000, Australia

**Privacy Officer.** Budgie's Privacy Officer is accountable for our compliance with this policy and with applicable privacy laws, and can be reached at support@tap-app.com.au.
