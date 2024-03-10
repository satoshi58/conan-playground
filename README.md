# CONAN PLAYGROUND

You can easily tests pkg installation with CONAN PLAYGROUND

# Requirement

conan 1.x

# Usage

Install, build and create pkg according to your update scenario.

## Example of scenario

minor version conflict 

- alpha : 1.0.0 (push to cache) 
- beta : 1.0.0 (push to cache)
    - specify alpha [^1.0.0]
    - refer to alpha 1.0.0
- alpha : 1.1.0 (push to cache) 
- gamma : 1.0.0 (push to cache) 
    - specify alpha [^1.0.0]
    - refer to alpha 1.1.0
- delta : 1.0.0 (pkg install) 
    - specify beta [^1.0.0] and gamma [^1.0.0]
    - refer to beta 1.0.0 and gamma 1.0.0

## pkg install, build and pkg creation

```bash
cd <pkg>
conan install .
mkdir -p _build && conan build .
conan create .
```

# Note

conan-playground have to be installed on /home/user.  
Otherwise conanfile.py on each pkg need to be modified.
