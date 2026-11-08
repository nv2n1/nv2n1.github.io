---
title: "Printing to STDERR and STDOUT in Perl"
date: 2018-03-24 11:53:05 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-print-a-line-to-stderr-and-stdout-in-perl/
---

Perl gives you straightforward ways to send output to both standard output and standard error. Understanding the difference matters — STDOUT handles normal program output, while STDERR carries diagnostics, warnings, and error messages. Separating them lets users redirect, log, or suppress errors independently.

## Basic Output Methods

The simplest approach uses `print` with filehandles:

``` perl
print STDOUT "This goes to standard output\n";
print STDERR "This is an error message\n";
```

When you call `print` without specifying a filehandle, it defaults to STDOUT:

``` perl
print "Normal output\n";  # Same as: print STDOUT "Normal output\n";
```

## Printing to Both Streams

Send output to both STDOUT and STDERR by making two separate calls:

``` perl
my $message = "Important information";
print STDOUT "$message\n";
print STDERR "$message\n";
```

For cleaner code when handling multiple messages, you might use a helper function:

``` perl
sub notify {
    my ($msg) = @_;
    print STDOUT "$msg\n";
    print STDERR "$msg\n";
}

notify("System started");
```

## Using warn() for STDERR

Perl’s `warn()` function automatically writes to STDERR and adds a newline:

``` perl
warn "This warning goes to STDERR\n";
```

You can capture and handle warnings with signal handlers:

``` perl
$SIG{__WARN__} = sub {
    my ($msg) = @_;
    # Custom warning handling
    print STDOUT "Warning caught: $msg";
};

warn "This triggers the handler";
```

## Flushing Output

Buffering can delay output to STDERR. Force immediate output by setting autoflush:

``` perl
use IO::Handle;

STDOUT->autoflush(1);
STDERR->autoflush(1);

print STDERR "Immediate error\n";
```

Or disable buffering for a single filehandle:

``` perl
{
    local $| = 1;  # $| enables autoflush for currently selected filehandle
    print STDERR "This appears immediately\n";
}
```

## Real-World Example

Here’s a practical pattern for logging errors while maintaining normal output:

``` perl
#!/usr/bin/perl
use strict;
use warnings;
use IO::Handle;

STDERR->autoflush(1);

sub log_error {
    my ($code, $message) = @_;
    print STDERR "[ERROR $code] $message\n";
    return 0;
}

sub log_info {
    my ($message) = @_;
    print STDOUT "[INFO] $message\n";
    return 1;
}

# Usage
log_info("Processing started");

unless (open my $fh, '<', 'config.txt') {
    log_error(1, "Cannot read config: $!");
    exit 1;
}

log_info("Configuration loaded successfully");
close $fh;
```

## Redirecting at Runtime

Users can redirect streams at the shell level without changing your code:

``` bash
# Send only errors to a file
perl script.pl 2> errors.log

# Send both stdout and stderr to the same file
perl script.pl &> output.log

# Suppress STDERR
perl script.pl 2> /dev/null

# Send STDERR to STDOUT for piping
perl script.pl 2>&1 | grep "ERROR"
```

## Duplicating Output

To write to both streams and a file simultaneously, use `Tee::Tiny` or implement it manually:

``` perl
use Tee::Tiny;

my $tee = Tee::Tiny->new;

# Output goes to STDOUT, STDERR, and file simultaneously
$tee->to_file("output.log");
print "This line appears everywhere\n";
```

Or without a module:

``` perl
open my $log, '>>', 'app.log' or die "Cannot open log: $!";

sub tee_output {
    my ($msg) = @_;
    print STDOUT $msg;
    print STDERR $msg;
    print $log $msg;
}

tee_output("Logged to all streams\n");
close $log;
```

## Error Handling Best Practices

Always use STDERR for diagnostics and reserve STDOUT for program output. This separation allows downstream tools to handle errors independently:

``` perl
#!/usr/bin/perl
use strict;
use warnings;

my $result = process_data();

if ($result) {
    print "Success: Data processed\n";  # STDOUT
} else {
    print STDERR "Error: Processing failed\n";  # STDERR
    exit 1;
}
```

When writing modules or scripts that will be piped or redirected, respecting this convention prevents mixing error messages with data output, making logs and automation more reliable.
