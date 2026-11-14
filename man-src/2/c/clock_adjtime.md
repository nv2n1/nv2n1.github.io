---
title: "clock_adjtime(2)"
name: "clock_adjtime"
section: "2"
letter: "c"
url: "/docs/linux/man/2-clock_adjtime/"
description: "adjtimex, clock_adjtime, ntp_adjtime – tune kernel clock"
---

<h2 class="name">NAME</h2>
<p> adjtimex, clock_adjtime, ntp_adjtime &#8211; tune kernel clock </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/timex.h&gt;
int adjtimex(struct timex *buf);
int clock_adjtime(clockid_t clk_id, struct timex *buf);
int ntp_adjtime(struct timex *buf);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Linux uses David L. Mills&#8217; clock adjustment algorithm (see RFC 5905). The system call <code>adjtimex</code>() reads and optionally sets adjustment parameters for this algorithm. It takes a pointer to a <i>timex</i> structure, updates kernel parameters from (selected) field values, and returns the same structure updated with the current kernel values. This structure is declared as follows: </p>
<p> struct timex {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;modes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Mode selector&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long offset;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Time offset;&nbsp;nanoseconds, if STA_NANO<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;status flag is set, otherwise<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;microseconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long freq;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Frequency offset;&nbsp;see NOTES for units&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long maxerror;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Maximum error&nbsp;(microseconds)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long esterror;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Estimated error&nbsp;(microseconds)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;status;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Clock command/status&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long constant;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PLL&nbsp;(phase-locked loop)&nbsp;time constant&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long precision;&nbsp;<wbr>&nbsp;/*&nbsp;Clock precision<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(microseconds, read-only)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long tolerance;&nbsp;<wbr>&nbsp;/*&nbsp;Clock frequency tolerance&nbsp;(read-only);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;see NOTES for units&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timeval time;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Current time&nbsp;(read-only, except for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ADJ_SETOFFSET);&nbsp;upon return, time.tv_usec<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;contains nanoseconds, if STA_NANO status<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flag is set, otherwise microseconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long tick;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Microseconds between clock ticks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long ppsfreq;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PPS&nbsp;(pulse per second)&nbsp;frequency<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(read-only);&nbsp;see NOTES for units&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long jitter;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PPS jitter&nbsp;(read-only);&nbsp;nanoseconds, if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STA_NANO status flag is set, otherwise<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;microseconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;shift;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PPS interval duration<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(seconds, read-only)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long stabil;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PPS stability&nbsp;(read-only);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;see NOTES for units&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long jitcnt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PPS count of jitter limit exceeded<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;events&nbsp;(read-only)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long calcnt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PPS count of calibration intervals<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(read-only)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long errcnt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PPS count of calibration errors<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(read-only)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long stbcnt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PPS count of stability limit exceeded<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;events&nbsp;(read-only)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tai;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;TAI offset, as set by previous ADJ_TAI<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;operation&nbsp;(seconds, read-only,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;since Linux 2.6.26)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Further padding bytes to allow for future expansion&nbsp;*/ }; </p>
<p> The <i>modes</i> field determines which parameters, if any, to set. (As described later in this page, the constants used for <code>ntp_adjtime</code>() are equivalent but differently named.) It is a bit mask containing a bitwise-<i>or</i> combination of zero or more of the following bits:</p>
<dl>
<dt><code>ADJ_OFFSET</code></p>
<dd> Set time offset from <i>buf.offset</i>. Since Linux 2.6.26, the supplied value is clamped to the range (-0.5s, +0.5s). In older kernels, an <code>EINVAL</code> error occurs if the supplied value is out of range.</p>
<dt><code>ADJ_FREQUENCY</code></p>
<dd> Set frequency offset from <i>buf.freq</i>. Since Linux 2.6.26, the supplied value is clamped to the range (-32768000, +32768000). In older kernels, an <code>EINVAL</code> error occurs if the supplied value is out of range.</p>
<dt><code>ADJ_MAXERROR</code></p>
<dd> Set maximum time error from <i>buf.maxerror</i>.</p>
<dt><code>ADJ_ESTERROR</code></p>
<dd> Set estimated time error from <i>buf.esterror</i>.</p>
<dt><code>ADJ_STATUS</code></p>
<dd> Set clock status bits from <i>buf.status</i>. A description of these bits is provided below.</p>
<dt><code>ADJ_TIMECONST</code></p>
<dd> Set PLL time constant from <i>buf.constant</i>. If the <code>STA_NANO</code> status flag (see below) is clear, the kernel adds 4 to this value.</p>
<dt><code>ADJ_SETOFFSET</code> (since Linux 2.6.39)</p>
<dd> Add <i>buf.time</i> to the current time. If <i>buf.status</i> includes the <code>ADJ_NANO</code> flag, then <i>buf.time.tv_usec</i> is interpreted as a nanosecond value; otherwise it is interpreted as microseconds.</p>
<dt>
<dd> The value of <i>buf.time</i> is the sum of its two fields, but the field <i>buf.time.tv_usec</i> must always be nonnegative. The following example shows how to normalize a <i>timeval</i> with nanosecond resolution.</p>
<dt>
<dd> while (buf.time.tv_usec &lt; 0) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf.time.tv_sec&nbsp;<wbr>&nbsp;-=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf.time.tv_usec&nbsp;+=&nbsp;1000000000; }</p>
<dt><code>ADJ_MICRO</code> (since Linux 2.6.26)</p>
<dd> Select microsecond resolution.</p>
<dt><code>ADJ_NANO</code> (since Linux 2.6.26)</p>
<dd> Select nanosecond resolution. Only one of <code>ADJ_MICRO</code> and <code>ADJ_NANO</code> should be specified.</p>
<dt><code>ADJ_TAI</code> (since Linux 2.6.26)</p>
<dd> Set TAI (Atomic International Time) offset from <i>buf.constant</i>.</p>
<dt>
<dd> <code>ADJ_TAI</code> should not be used in conjunction with <code>ADJ_TIMECONST</code>, since the latter mode also employs the <i>buf.constant</i> field.</p>
<dt>
<dd> For a complete explanation of TAI and the difference between TAI and UTC, see <i>BIPM</i></p>
<dt><code>ADJ_TICK</code></p>
<dd> Set tick value from <i>buf.tick</i>.</dl>
<p> Alternatively, <i>modes</i> can be specified as either of the following (multibit mask) values, in which case other bits should not be specified in <i>modes</i>:</p>
<dl>
<dt><code>ADJ_OFFSET_SINGLESHOT</code></p>
<dd> Old-fashioned <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3): (gradually) adjust time by value specified in <i>buf.offset</i>, which specifies an adjustment in microseconds.</p>
<dt><code>ADJ_OFFSET_SS_READ</code> (functional since Linux 2.6.28)</p>
<dd> Return (in <i>buf.offset</i>) the remaining amount of time to be adjusted after an earlier <code>ADJ_OFFSET_SINGLESHOT</code> operation. This feature was added in Linux 2.6.24, but did not work correctly until Linux 2.6.28.</dl>
<p> Ordinary users are restricted to a value of either 0 or <code>ADJ_OFFSET_SS_READ</code> for <i>modes</i>. Only the superuser may set any parameters. </p>
<p> The <i>buf.status</i> field is a bit mask that is used to set and/or retrieve status bits associated with the NTP implementation. Some bits in the mask are both readable and settable, while others are read-only.</p>
<dl>
<dt><code>STA_PLL</code> (read-write)</p>
<dd> Enable phase-locked loop (PLL) updates via <code>ADJ_OFFSET</code>.</p>
<dt><code>STA_PPSFREQ</code> (read-write)</p>
<dd> Enable PPS (pulse-per-second) frequency discipline.</p>
<dt><code>STA_PPSTIME</code> (read-write)</p>
<dd> Enable PPS time discipline.</p>
<dt><code>STA_FLL</code> (read-write)</p>
<dd> Select frequency-locked loop (FLL) mode.</p>
<dt><code>STA_INS</code> (read-write)</p>
<dd> Insert a leap second after the last second of the UTC day, thus extending the last minute of the day by one second. Leap-second insertion will occur each day, so long as this flag remains set.</p>
<dt><code>STA_DEL</code> (read-write)</p>
<dd> Delete a leap second at the last second of the UTC day. Leap second deletion will occur each day, so long as this flag remains set.</p>
<dt><code>STA_UNSYNC</code> (read-write)</p>
<dd> Clock unsynchronized.</p>
<dt><code>STA_FREQHOLD</code> (read-write)</p>
<dd> Hold frequency. Normally adjustments made via <code>ADJ_OFFSET</code> result in dampened frequency adjustments also being made. So a single call corrects the current offset, but as offsets in the same direction are made repeatedly, the small frequency adjustments will accumulate to fix the long-term skew.</p>
<dt>
<dd> This flag prevents the small frequency adjustment from being made when correcting for an <code>ADJ_OFFSET</code> value.</p>
<dt><code>STA_PPSSIGNAL</code> (read-only)</p>
<dd> A valid PPS (pulse-per-second) signal is present.</p>
<dt><code>STA_PPSJITTER</code> (read-only)</p>
<dd> PPS signal jitter exceeded.</p>
<dt><code>STA_PPSWANDER</code> (read-only)</p>
<dd> PPS signal wander exceeded.</p>
<dt><code>STA_PPSERROR</code> (read-only)</p>
<dd> PPS signal calibration error.</p>
<dt><code>STA_CLOCKERR</code> (read-only)</p>
<dd> Clock hardware fault.</p>
<dt><code>STA_NANO</code> (read-only; since Linux 2.6.26)</p>
<dd> Resolution (0 = microsecond, 1 = nanoseconds). Set via <code>ADJ_NANO</code>, cleared via <code>ADJ_MICRO</code>.</p>
<dt><code>STA_MODE</code> (since Linux 2.6.26)</p>
<dd> Mode (0 = Phase Locked Loop, 1 = Frequency Locked Loop).</p>
<dt><code>STA_CLK</code> (read-only; since Linux 2.6.26)</p>
<dd> Clock source (0 = A, 1 = B); currently unused.</dl>
<p> Attempts to set read-only <i>status</i> bits are silently ignored.</p>
<h3>clock_adjtime ()</h3>
<p> The <code>clock_adjtime</code>() system call (added in Linux 2.6.39) behaves like <code>adjtimex</code>() but takes an additional <i>clk_id</i> argument to specify the particular clock on which to act.</p>
<h3>ntp_adjtime ()</h3>
<p> The <code>ntp_adjtime</code>() library function (described in the NTP &quot;Kernel Application Program API&quot;, KAPI) is a more portable interface for performing the same task as <code>adjtimex</code>(). Other than the following points, it is identical to <code>adjtimex</code>():</p>
<dl>
<dt>*</p>
<dd> The constants used in <i>modes</i> are prefixed with &quot;MOD_&quot; rather than &quot;ADJ_&quot;, and have the same suffixes (thus, <code>MOD_OFFSET</code>, <code>MOD_FREQUENCY</code>, and so on), other than the exceptions noted in the following points.</p>
<dt>*</p>
<dd> <code>MOD_CLKA</code> is the synonym for <code>ADJ_OFFSET_SINGLESHOT</code>.</p>
<dt>*</p>
<dd> <code>MOD_CLKB</code> is the synonym for <code>ADJ_TICK</code>.</p>
<dt>*</p>
<dd> The is no synonym for <code>ADJ_OFFSET_SS_READ</code>, which is not described in the KAPI.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>adjtimex</code>() and <code>ntp_adjtime</code>() return the clock state; that is, one of the following values:</p>
<dl>
<dt><code>TIME_OK</code></p>
<dd> Clock synchronized, no leap second adjustment pending.</p>
<dt><code>TIME_INS</code></p>
<dd> Indicates that a leap second will be added at the end of the UTC day.</p>
<dt><code>TIME_DEL</code></p>
<dd> Indicates that a leap second will be deleted at the end of the UTC day.</p>
<dt><code>TIME_OOP</code></p>
<dd> Insertion of a leap second is in progress.</p>
<dt><code>TIME_WAIT</code></p>
<dd> A leap-second insertion or deletion has been completed. This value will be returned until the next <code>ADJ_STATUS</code> operation clears the <code>STA_INS</code> and <code>STA_DEL</code> flags.</p>
<dt><code>TIME_ERROR</code></p>
<dd> The system clock is not synchronized to a reliable server. This value is returned when any of the following holds true:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Either <code>STA_UNSYNC</code> or <code>STA_CLOCKERR</code> is set.</p>
<dt>*</p>
<dd> <code>STA_PPSSIGNAL</code> is clear and either <code>STA_PPSFREQ</code> or <code>STA_PPSTIME</code> is set.</p>
<dt>*</p>
<dd> <code>STA_PPSTIME</code> and <code>STA_PPSJITTER</code> are both set.</p>
<dt>*</p>
<dd> <code>STA_PPSFREQ</code> is set and either <code>STA_PPSWANDER</code> or <code>STA_PPSJITTER</code> is set.</dl>
</dl>
<dt>
<dd> The symbolic name <code>TIME_BAD</code> is a synonym for <code>TIME_ERROR</code>, provided for backward compatibility.</dl>
<p> Note that starting with Linux 3.4, the call operates asynchronously and the return value usually will not reflect a state change caused by the call itself. </p>
<p> On failure, these calls return -1 and set <i>errno</i>.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>buf</i> does not point to writable memory.</p>
<dt><code>EINVAL</code> (kernels before Linux 2.6.26)</p>
<dd> An attempt was made to set <i>buf.freq</i> to a value outside the range (-33554432, +33554432).</p>
<dt><code>EINVAL</code> (kernels before Linux 2.6.26)</p>
<dd> An attempt was made to set <i>buf.offset</i> to a value outside the permitted range. In kernels before Linux 2.0, the permitted range was (-131072, +131072). From Linux 2.0 onwards, the permitted range was (-512000, +512000).</p>
<dt><code>EINVAL</code></p>
<dd> An attempt was made to set <i>buf.status</i> to a value other than those listed above.</p>
<dt><code>EINVAL</code></p>
<dd> The <i>clk_id</i> given to <code>clock_adjtime</code>() is invalid for one of two reasons. Either the System-V style hard-coded positive clock ID value is out of range, or the dynamic <i>clk_id</i> does not refer to a valid instance of a clock object. See <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) for a discussion of dynamic clocks.</p>
<dt><code>EINVAL</code></p>
<dd> An attempt was made to set <i>buf.tick</i> to a value outside the range 900000/<code>HZ</code> to 1100000/<code>HZ</code>, where <code>HZ</code> is the system timer interrupt frequency.</p>
<dt><code>ENODEV</code></p>
<dd> The hot-pluggable device (like USB for example) represented by a dynamic <i>clk_id</i> has disappeared after its character device was opened. See <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) for a discussion of dynamic clocks.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The given <i>clk_id</i> does not support adjustment.</p>
<dt><code>EPERM</code></p>
<dd> <i>buf.modes</i> is neither 0 nor <code>ADJ_OFFSET_SS_READ</code>, and the caller does not have sufficient privilege. Under Linux, the <code>CAP_SYS_TIME</code> capability is required.</dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ntp_adjtime</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> None of these interfaces is described in POSIX.1 </p>
<p> <code>adjtimex</code>() and <code>clock_adjtime</code>() are Linux-specific and should not be used in programs intended to be portable. </p>
<p> The preferred API for the NTP daemon is <code>ntp_adjtime</code>().</p>
<h2>NOTES</h2>
<p> In struct <i>timex</i>, <i>freq</i>, <i>ppsfreq</i>, and <i>stabil</i> are ppm (parts per million) with a 16-bit fractional part, which means that a value of 1 in one of those fields actually means 2^-16 ppm, and 2^16=65536 is 1 ppm. This is the case for both input values (in the case of <i>freq</i>) and output values. </p>
<p> The leap-second processing triggered by <code>STA_INS</code> and <code>STA_DEL</code> is done by the kernel in timer context. Thus, it will take one tick into the second for the leap second to be inserted or deleted.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2), <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3), <code><a href="/docs/linux/man/3-ntp_gettime/">ntp_gettime</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7), <code><a href="/docs/linux/man/8-adjtimex/">adjtimex</a></code>(8), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) </p>
<p> NTP &quot;Kernel Application Program Interface&quot;</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
