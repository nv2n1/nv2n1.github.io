---
title: "krb5_string_to_deltat(3)"
name: "krb5_string_to_deltat"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_string_to_deltat/"
description: "krb5_timeofday krb5_set_real_time krb5_us_timeofday krb5_format_time krb5_string_to_deltat – Kerberos 5 time handling functions"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_timeofday</code> <code>krb5_set_real_time</code> <code>krb5_us_timeofday</code> <code>krb5_format_time</code> <code>krb5_string_to_deltat</code> &#8211; Kerberos 5 time handling functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h </p>
<p> <code>krb5_timestamp</code> </p>
<p> <code>krb5_deltat</code> Ft krb5_error_code Fo krb5_set_real_time Fa krb5_context context Fa krb5_timestamp sec Fa int32_t usec Fc Ft krb5_error_code Fo krb5_timeofday Fa krb5_context context Fa krb5_timestamp *timeret Fc Ft krb5_error_code Fo krb5_us_timeofday Fa krb5_context context Fa krb5_timestamp *sec Fa int32_t *usec Fc Ft krb5_error_code Fo krb5_format_time Fa krb5_context context Fa time_t t Fa char *s Fa size_t len Fa krb5_boolean include_time Fc Ft krb5_error_code Fo krb5_string_to_deltat Fa const char *string Fa krb5_deltat *deltat Fc</p>
<h2>DESCRIPTION</h2>
<p> <code>krb5_set_real_time</code> sets the absolute time that the caller knows the KDC has. With this the Kerberos library can calculate the relative difference between the KDC time and the local system time and store it in the Fa context . With this information the Kerberos library can adjust all time stamps in Kerberos packages. </p>
<p> Fn krb5_timeofday returns the current time, but adjusted with the time difference between the local host and the KDC. Fn krb5_us_timeofday also returns microseconds. </p>
<p> <code>krb5_format_time</code> formats the time Fa t into the string Fa s of length Fa len . If Fa include_time is set, the time is set include_time. </p>
<p> <code>krb5_string_to_deltat</code> parses delta time Fa string into Fa deltat .</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a>(2), <a href="/docs/linux/man/3-krb5/">krb5</a>(3) </p>
<h2>Index</h2>
