---
title: "Running Commands Across Multiple Linux Servers in Parallel"
date: 2016-01-03 08:36:52 +0000
modified: 2026-04-11 17:16:05 +0000
author: "Eric Ma"
layout: post
categories: [web-development]
canonical: /three-methods-execute-commands-many-nodes-parallel-ssh-linux/
---

Running commands across multiple servers is fundamental to cluster management and infrastructure automation. While orchestration tools like Ansible and Terraform dominate modern deployments, sometimes you need lightweight solutions that work without dependencies—or you’re already invested in SSH-based infrastructure.

When managing clusters, you typically work in two modes: serial execution (one node at a time) and parallel execution (multiple nodes simultaneously). Serial execution is straightforward to debug; parallel execution is faster and better for time-sensitive operations.

Here are three practical methods using standard Linux tools.

## Bash loops for SSH execution

Bash is always available, making it the most portable option. It’s effective for small clusters or when you need conditional logic between commands.

**Serial execution:**

``` bash
for h in lnode31 lnode6 cluster1-{1..8}; do
    ssh root@$h hostname
done
```

**Parallel execution:**

``` bash
for h in lnode31 lnode6 cluster1-{1..8}; do
    ssh root@$h hostname &
done
wait
```

The `&` backgrounds each SSH process. The `wait` command ensures the script doesn’t exit until all background jobs complete. This approach scales reasonably for dozens of nodes but becomes unwieldy with hundreds.

**Advantages:** No additional packages. Easy to add error handling:

``` bash
for h in lnode31 lnode6 cluster1-{1..8}; do
    if ssh root@$h hostname; then
        echo "$h: OK"
    else
        echo "$h: FAILED"
    fi &
done
wait
```

**Disadvantages:** Output can interleave unpredictably. Managing dozens of simultaneous SSH connections requires tuning SSH settings. No built-in output aggregation.

## Clustershell (clush)

Clustershell is purpose-built for parallel cluster operations. It handles connection pooling, output formatting, and result aggregation efficiently.

Install on Fedora/RHEL:

``` bash
sudo dnf install clustershell
```

On Ubuntu/Debian:

``` bash
sudo apt install clustershell
```

**Execute across multiple nodes:**

``` bash
clush -l root -w lnode31,lnode6,cluster1-[1-8] hostname
```

Output is automatically grouped by result, making it easy to spot differences:

    lnode31: lnode31
    lnode6: lnode6
    cluster1-[1-8]: cluster1-1
    cluster1-2
    ...

For interactive commands (copy files, run interactive shells):

``` bash
clush -l root -w lnode31,lnode6,cluster1-[1-8] --copy /etc/config
clush -l root -w lnode31,lnode6,cluster1-[1-8] -i  # interactive shell
```

Configure persistent node groups in `/etc/clustershell/groups`:

    webservers: lnode31,lnode6,cluster1-[1-8]

Then use: `clush -l root -w @webservers hostname`

**Advantages:** Designed for large clusters. Smart output grouping. Connection pooling. Persistent configuration. Interactive mode for troubleshooting.

**Disadvantages:** Requires installation. Steeper learning curve than Bash loops.

## PDSH

PDSH is a lightweight parallel remote shell that supports multiple backends beyond SSH (useful in heterogeneous environments).

Install on Fedora/RHEL:

``` bash
sudo dnf install pdsh pdsh-rcmd-ssh
```

On Ubuntu/Debian:

``` bash
sudo apt install pdsh
```

**Execute across multiple nodes:**

``` bash
pdsh -R ssh -l root -w lnode31,lnode6,cluster1-[1-8] hostname
```

The `-R ssh` flag specifies SSH as the rcmd module. PDSH defaults to rsh if you omit it (which is rarely what you want).

Control parallelism with `-f`:

``` bash
pdsh -R ssh -f 10 -l root -w @allnodes uptime  # max 10 parallel connections
```

Use fanout to prevent overwhelming networks:

``` bash
pdsh -R ssh -f 5 -l root -w lnode31,lnode6,cluster1-[1-8] 'find / -name "*.log" -mtime +30 -delete'
```

**Advantages:** Lightweight binary. Faster than clustershell for very large clusters. Supports other rcmd modules (useful for legacy rsh environments). Low overhead.

**Disadvantages:** Less sophisticated output grouping than clustershell. Smaller community and fewer active updates than Ansible/parallel tools.

## Comparison and recommendations

Use **Bash** for ad-hoc one-offs on small clusters (\< 20 nodes) where dependencies are a problem.

Use **clustershell** for regular cluster operations and large deployments (100+ nodes). The configuration persistence and output grouping pay off quickly.

Use **PDSH** when you need minimal overhead or support for non-SSH protocols, or when operating in environments where systemd/containers might interfere with SSH multiplexing.

For new infrastructure, consider **Ansible** or **GNU Parallel** instead. Ansible provides better idempotency and state management. GNU Parallel offers more flexible command generation and is excellent for batch processing.

These three SSH-based methods remain useful in constrained environments, but they’re increasingly supplemented by configuration management tools in production clusters.
