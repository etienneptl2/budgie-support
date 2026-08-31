---
title: Privacy Policy
layout: default
---

# Privacy Policy
**Budgie**
_Last updated: 15 August 2026_

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

We do **not** sell your personal or financial data to any third party, and we do **not** allow any third party to use your budgeting data to train AI models.

---

## 5. Advertising & Your Choices
You can manage how ads are personalized:
- On **iOS**, you can change tracking permission in your device’s Settings, and review your choices via **Settings → Privacy options** in the App (where available).
- On **Android**, you can reset or limit your advertising ID in your device settings.
- In the EEA/UK, you can re‑open the consent form at any time via **Settings → Privacy options**.

---

## 6. Your Privacy Rights
Depending on where you live, you may have some or all of the following rights in relation to the personal information we hold about you:
- **Access** the personal information we hold about you
- **Correct** inaccurate or incomplete information
- **Delete** your account and associated data
- **Opt out** of personalized advertising
- **Opt out** of AI insights, by turning the feature off in **Profile → AI insights**
- **Withdraw consent** where our processing relies on your consent
- **Lodge a complaint** with your local privacy regulator

To exercise any of these rights, use the in‑app controls (for example **Settings → Delete account**) or contact us (see Section 12). Some rights, and the way they apply, depend on the privacy laws of your country — see Section 7.

---

## 7. Applicable Privacy Laws
Budgie is offered internationally. The privacy laws that apply to you depend on where you live.

### Australia
We handle your information in accordance with the **Australian Privacy Act 1988** and the **Australian Privacy Principles (APPs)**. If you are in Australia and have a privacy complaint, you may contact us (see Section 12) and, if unsatisfied, lodge a complaint with the **Office of the Australian Information Commissioner (OAIC)** at [oaic.gov.au](https://www.oaic.gov.au).

### United States (including California)
We do **not** sell your personal information. If you are a California resident, you may have rights under the **California Consumer Privacy Act (CCPA/CPRA)**, including to know what personal information we process, to request its deletion, and to opt out of personalized advertising. You can limit ad personalization using the choices described in Section 5.

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

---

## 10. Data Security & International Transfers
Data handled through **Google Firebase / Firestore** is **encrypted in transit** (using TLS) and **encrypted at rest** on Google’s servers, using the security measures provided by Google. This is standard server‑side encryption; it is **not** end‑to‑end encryption, which means the providers that operate these services are technically able to access the data in order to run them. On your device, budgeting data is protected by your device’s standard operating‑system protections.

Summaries sent for **AI insights** travel over an encrypted (TLS) connection to our server function and on to OpenAI, and are processed on OpenAI's servers in the **United States**.

Because Google, Apple, OpenAI, and our other providers operate globally, your information may be stored or processed on servers located **outside your country**, including in countries whose data‑protection laws differ from your own. We use established, widely‑used providers and take reasonable steps to protect your information. However, no method of transmission or storage is completely secure, and we cannot guarantee absolute security.

---

## 11. Updates to This Policy
This Privacy Policy may be updated periodically. Any changes take effect once posted within the App or on this page. The “Last updated” date above reflects the latest revision.

---

## 12. Contact
If you have questions about this Privacy Policy or wish to exercise your privacy rights, please contact us:

📧 **support@tap-app.com.au**
