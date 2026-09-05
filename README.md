# Budgie — Support

Thanks for using **Budgie**!

If you need help, have feedback, or want to report an issue, please contact:

📧 **Email:** support@tap-app.com.au

---

## FAQ

### The app freezes or doesn’t work properly.

Try closing and reopening the app.  
If the issue continues, please email support with details about your device model and OS version.

### I want to request a feature.

Feature ideas are always welcome!  
Send your suggestion via email and the team will review it for future updates.

### Does the app collect data?

Your budgeting data is stored **locally on your device** by default, and the App is free to use without an account.

If you subscribe to **Budgie Pro**, **sign in** (with Apple or Google), and turn on **cloud sync**, your data is stored in Google Firebase so it can sync across your devices. The free App displays ads via Google AdMob. See the [Privacy Policy](./privacy.md) for full details. You can delete your account and data at any time in Settings → Delete account.

### What are AI insights, and what gets sent?

**AI insights** are short cards about your spending, written by an AI model from OpenAI. The feature is **off by default** — nothing is sent unless you turn on **Profile → AI insights** while signed in.

When it's on, Budgie sends **aggregated totals** — monthly income and spending, per‑category totals, and your budgets and goals (including the names you gave them). Your **notes and individual transactions never leave your device**, nothing identifying you is sent to OpenAI, and your data is **not used to train any AI model**. Turning the switch off deletes the cards on your device. See section 2.7 of the [Privacy Policy](./privacy.md).

### What is Budgie Pro?

**Budgie Pro** is an optional subscription that unlocks **cloud sync** across your devices and **removes ads**. It's available as a **monthly** or **yearly** auto‑renewing subscription, billed through the App Store or Google Play.

### How do I manage or cancel my subscription?

Open **Settings → Manage subscription** in the app (this opens your store's subscription sheet), or manage it directly in your **Apple App Store** or **Google Play** account settings.

### I paid for Budgie Pro but don't see it (new device or reinstall).

Open **Settings → Restore purchases**. Make sure you're signed in with the same Apple or Google account you used to purchase, and the same Budgie account you subscribed with.

---

## About This Page

This repository hosts the official support page for the **Budgie** mobile application.

---

## Legal

[Privacy Policy](./privacy.md) · [Terms of Use (EULA)](./terms.md)

`terms.md` is the source of truth for the EULA. The app links to the published
page, but App Store Connect keeps its own **pasted copy** — its custom licence
agreement is a plain-text field, not a URL. After changing `terms.md`, regenerate
the paste-ready text and copy it into App Store Connect (Apps → Budgie → General
→ App Information → License Agreement), or the two will drift apart:

```bash
python3 scripts/build-eula-text.py
```

That rewrites [`terms-appstore.txt`](./terms-appstore.txt); don't edit it by hand.
`--check` exits non-zero when it is stale.
