---
title: "mcs(8)"
name: "mcs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mcs/"
---

mcs - Multi-Category System

<h2>Description</h2>

MCS (Multiple Category System) allows users to label files on their system within administrator defined categories. It then uses SELinux Mandatory Access Control to protect those files. MCS is a discretionary model to allow users to mark their data with additional tags that further restrict access. The only mandatory aspect is authorizing users for categories by defining their clearance in policy. However, MCS is similar to MLS and exercises the same code paths and share the same support infrastructure. They just differ in their specific configuration. The <i>/etc/selinux/{SELINUXTYPE}/setrans.conf configuration file translates the labels on disk to human</i> readable form. Administrators can define any labels they want in this file. Certain applications like printing and auditing will use these labels to identify the files. By setting a category on a file you will prevent other applications/services from having access to the files. Examples of file labels would be PatientRecord, CompanyConfidential etc. 

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-selinux/">selinux</a>(8), <a HREF="/docs/linux/man/1-chcon/">chcon</a>(1) 

<h2>Files</h2>

/etc/selinux/{SELINUXTYPE}/setrans.conf
