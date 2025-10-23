# Satori

This is a custom OS based on Fedora Atomic.

## Installation

```bash
sudo bootc switch ghcr.io/mradityaalok/<variant_name>
```

```
```

- Reboot again to complete the installation

  ```
  systemctl reboot
  ```

## Verification

These images are signed with [Sigstore](https://www.sigstore.dev/)'s [cosign](https://github.com/sigstore/cosign). You can verify the signature by downloading the `cosign.pub` file from this repo and running the following command:

```bash
cosign verify --key cosign.pub ghcr.io/mradityaalok/satori
```
