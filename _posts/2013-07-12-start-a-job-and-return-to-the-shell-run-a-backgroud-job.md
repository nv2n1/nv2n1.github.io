---
title: "Start a Background Job and Return to the Shell"
date: 2013-07-12 16:31:53 +0000
layout: post
canonical: https://www.systutorials.com/start-a-job-and-return-to-the-shell-run-a-backgroud-job/
---

When you need to start long-running commands while continuing to work in the shell, run them in the background. Bash and other modern shells maintain a job list and allow you to switch jobs between foreground and background execution. Only one job can run in the foreground at a time.

## Starting a Background Job

Append `&` to any command to run it in the background:

``` bash
command &
```

The shell returns the prompt immediately without waiting for the command to complete. Without `&`, you’d be blocked at the shell prompt until the command finishes.

Example:

``` bash
tar -czf backup.tar.gz /home/user/documents &
find / -name "*.log" -mtime +30 > old_logs.txt &
```

Both commands now run in the background while you retain shell control.

## Moving a Running Foreground Job to the Background

If you forgot the `&` and a job is consuming your foreground:

1.  Suspend the job with `Ctrl+Z`
2.  Resume it in the background:

``` bash
bg
```

Or specify a job number if multiple jobs are suspended:

``` bash
bg %1
```

## Listing Background Jobs

Use the `jobs` builtin to see all background and suspended jobs:

``` bash
jobs
```

Output example:

    [1]   Running                 tar -czf backup.tar.gz /home/user/documents &
    [2]-  Stopped                 find / -name "*.log" -mtime +30 > old_logs.txt
    [3]+  Running                 rsync -av /source /dest

Each job gets a number (in brackets) that you use for job control. The `+` marks the current job, and `-` marks the previous job.

Get more details with:

``` bash
jobs -l
```

This includes the process ID (PID) for each job.

## Bringing Jobs to the Foreground

Move a background job to the foreground with:

``` bash
fg %n
```

Replace `n` with the job number. For the current job (marked with `+`):

``` bash
fg
```

This is useful when you need to monitor output or interact with a running process.

## Moving a Suspended Job to the Background

Resume a suspended job in the background (without returning it to the foreground):

``` bash
bg %n
```

For example, if job 2 is stopped:

``` bash
bg %2
```

## Terminating Background Jobs

Kill a background job using its job number:

``` bash
kill %n
```

Example:

``` bash
kill %1
```

Or use the process ID directly (visible with `jobs -l`):

``` bash
kill 12345
```

Send a specific signal if the job ignores `SIGTERM`:

``` bash
kill -9 %n
```

For cleanup, force-kill all background jobs:

``` bash
killall tar
```

## Preventing Job Loss on Shell Exit

Background jobs terminate when you close the shell or log out. To keep a job running after logout, use `nohup`:

``` bash
nohup long_running_command > output.log 2>&1 &
```

Or use `disown` to remove a job from the shell’s job table:

``` bash
long_running_command &
disown %1
```

The job continues running but is no longer tracked by the shell.

## Waiting for Background Jobs

Wait for a specific background job to complete:

``` bash
wait %1
```

Wait for all background jobs:

``` bash
wait
```

This blocks the shell until the specified job or all jobs finish, useful in scripts.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Start a Background Job and Return to the Shell with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Start a Background Job and Return to the Shell. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
