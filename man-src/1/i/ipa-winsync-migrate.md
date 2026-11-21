---
title: "ipa-winsync-migrate(1)"
name: "ipa-winsync-migrate"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-winsync-migrate/"
description: "ipa-winsync-migrate – Seamless migration of AD users created by winsync to native AD users."
---

<h2>NAME</h2>
<p> ipa-winsync-migrate &#8211; Seamless migration of AD users created by winsync to native AD users.</p>
<h2>SYNOPSIS</h2>
<p> ipa-winsync-migrate</p>
<h2>DESCRIPTION</h2>
<p> Migrates AD users created by winsync agreement to ID overrides in the Default Trust View, thus preserving the actual POSIX attributes already established. </p>
<p> Prior to the actual migration, the winsync replication agreement will be removed to protect the removal of the user accounts on the Active Directory side. </p>
<p> During the migration, group, assigned roles, HBAC rules and SELinux memberships of the synced users will be preserved. Any local copies (created by winsync) of the migrated users will be removed. </p>
<h2>WARNINGS</h2>
<p> After the migration, any PassSync agreements need to be removed from Active Directory Domain Controllers, otherwise they might attempt to update passwords for accounts that no longer exist on the IPA server. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;realm</code></dt>
<dd> The Active Directory realm the winsynced users belong to.</dd>
<dt><code>&#8211;server</code></dt>
<dd> The hostname of Active Directory Domain Controller the winsync replication agreement is established with.</dd>
<dt><code>&#8211;unattended</code></dt>
<dd> Never prompts for user input. </dd>
</dl>
