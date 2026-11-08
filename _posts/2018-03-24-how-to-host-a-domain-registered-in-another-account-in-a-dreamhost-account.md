---
title: "Hosting a Domain from Another Account on Dreamhost"
date: 2018-03-24 08:18:01 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-host-a-domain-registered-in-another-account-in-a-dreamhost-account/
---

If you’re trying to add a domain to a Dreamhost account and get the error “You can’t add that domain: already in our system,” the domain is already configured for DNS hosting in another Dreamhost account. You need to remove the DNS hosting from the original account before you can host it elsewhere.

This process is safe—removing DNS hosting doesn’t delete your domain registration. The domain remains registered in the original account; you’re only stopping Dreamhost from managing its nameservers.

## Remove DNS Hosting from the Original Account

1.  Log into the Dreamhost account where the domain is currently registered
2.  Navigate to **Manage Domains**
3.  Find the domain in the list and click **Delete** next to it
4.  Confirm the deletion

The domain registration stays intact in that account. You’ve only removed the DNS hosting configuration.

## Add the Domain to Your New Account

Once you’ve deleted the DNS hosting from the original account, log into your new Dreamhost account and add the domain as you normally would. It should add without errors since the DNS hosting is no longer claimed by the other account.

## Important Considerations

**Nameserver Updates**: If you’re moving an active domain between accounts, you may need to update the nameservers at your registrar if you’re also planning to change DNS providers. Dreamhost typically uses nameservers like `ns1.dreamhost.com`, `ns2.dreamhost.com`, etc., but confirm the correct servers in your new account’s DNS panel.

**Email and DNS Records**: Before removing DNS hosting, note any custom DNS records, MX records for email, or other configurations in the original account. You’ll need to recreate these in the new account. Export or screenshot your DNS records first.

**Timing and Propagation**: DNS changes can take 4-48 hours to fully propagate. If the domain is actively used, plan this move during a maintenance window or low-traffic period.

**Keeping the Domain Registered Elsewhere**: If you want to keep the domain registered in the original Dreamhost account while hosting it in another account, that’s possible. You only need to update the nameservers at the registrar to point to the new hosting account’s nameservers. This works even if both accounts are with Dreamhost.

## Verifying the Move

After adding the domain to your new account, verify the nameservers are correct:

``` bash
nslookup -type=NS yourdomain.com
```

Or check through the Dreamhost control panel under **Manage Domains** to confirm DNS hosting is active in your new account.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
