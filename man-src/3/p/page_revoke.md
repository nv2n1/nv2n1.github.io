---
title: "page_revoke(3)"
name: "page_revoke"
section: "3"
letter: "p"
url: "/docs/linux/man/3-page_revoke/"
---

page_revoke - Revocation methods There are two revocation method for PKIX/X.509: CRL and OCSP. Revocation is needed if the private key is lost and stolen. Depending on how picky you are, you might want to make revocation for destroyed private keys too (smartcard broken), but that should not be a problem. CRL is a list of certifiates that have expired. OCSP is an online checking method where the requestor sends a list of certificates to the OCSP server to return a signed reply if they are valid or not. Some services sends a OCSP reply as part of the hand-shake to make the revoktion decision simpler/faster for the client. 
