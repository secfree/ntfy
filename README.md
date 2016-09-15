
## About

The original main project is here: [dschep/ntfy](https://github.com/dschep/ntfy).

I implemented send messages by `mailx`. Because in a company internal domain, use the `mailx` command to
send messages it the most convenient and secure way, whitout leak data outside the internal domain.

## Dependency

1. heirloom-mailx

## Configure

`~/.config/ntfy/ntfy.yml`:

```yml
---
backends:
    - mailx
mailx:
    receivers: "test@company.com"
```

## Example

```
$ ntfy -b mailx -t 'example' send 'test'
```