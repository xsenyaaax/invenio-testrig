# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-12-10 10:02:48 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 37 |
| **Patched Packages** | 4 |
| **Unpatched Packages** | 33 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 4 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 0 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [invenio-previewer](https://github.com/oarepo/invenio-previewer/tree/oarepo-feature-container-previewers) | https://github.com/oarepo/invenio-previewer | oarepo-feature-container-previewers |
| [invenio-records-resources](https://github.com/oarepo/invenio-records-resources/tree/oarepo-feature-extractors) | https://github.com/oarepo/invenio-records-resources | oarepo-feature-extractors |
| [invenio-rdm-records](https://github.com/oarepo/invenio-rdm-records/tree/oarepo-feature-zip) | https://github.com/oarepo/invenio-rdm-records | oarepo-feature-zip |
| [invenio-app-rdm](https://github.com/oarepo/invenio-app-rdm/tree/oarepo-feature-extract-preview-ui-links) | https://github.com/oarepo/invenio-app-rdm | oarepo-feature-extract-preview-ui-links |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `invenio-mail` | ⏭️  Skipped |
| `invenio-config` | ⏭️  Skipped |
| `invenio-queues` | ⏭️  Skipped |
| `invenio-oauthclient` | ⏭️  Skipped |
| `invenio-cache` | ⏭️  Skipped |
| `invenio-base` | ⏭️  Skipped |
| `invenio-theme` | ⏭️  Skipped |
| `invenio-assets` | ⏭️  Skipped |
| `invenio-celery` | ⏭️  Skipped |
| `invenio-pidstore` | ⏭️  Skipped |
| `invenio-db` | ⏭️  Skipped |
| `invenio-indexer` | ⏭️  Skipped |
| `invenio-oaiserver` | ⏭️  Skipped |
| `invenio-access` | ⏭️  Skipped |
| `invenio-rest` | ⏭️  Skipped |
| `invenio-records-permissions` | ⏭️  Skipped |
| `invenio-records-ui` | ⏭️  Skipped |
| `invenio-stats` | ⏭️  Skipped |
| `invenio-userprofiles` | ⏭️  Skipped |
| `invenio-search-ui` | ⏭️  Skipped |
| `invenio-records-files` | ⏭️  Skipped |
| `invenio-logging` | ⏭️  Skipped |
| `invenio-sitemap` | ⏭️  Skipped |
| `invenio-files-rest` | ⏭️  Skipped |
| `invenio-formatter` | ⏭️  Skipped |
| `invenio-records-rest` | ⏭️  Skipped |
| `invenio-i18n` | ⏭️  Skipped |
| `invenio-oauth2server` | ⏭️  Skipped |
| `invenio-jsonschemas` | ⏭️  Skipped |
| `invenio-search` | ⏭️  Skipped |
| `invenio-accounts` | ⏭️  Skipped |
| `invenio-webhooks` | ⏭️  Skipped |
| `invenio-records` | ⏭️  Skipped |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-banners` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-banners/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-banners/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-banners/test-report-patched.xml)<br>[warnings](packages/invenio-banners/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-notifications` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-notifications/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-notifications/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-notifications/test-report-patched.xml)<br>[warnings](packages/invenio-notifications/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-pages` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pages/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pages/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pages/test-report-patched.xml)<br>[warnings](packages/invenio-pages/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 18 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-banners` | 6 |
| `invenio-github` | 6 |
| `invenio-pages` | 6 |

#### Warning 2 - 6 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-banners` | 2 |
| `invenio-notifications` | 2 |
| `invenio-pages` | 2 |

#### Warning 3 - 6 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-banners` | 2 |
| `invenio-notifications` | 2 |
| `invenio-pages` | 2 |

#### Warning 4 - 6 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-pages` | 6 |

#### Warning 5 - 4 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 6 - 4 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-banners` | 2 |
| `invenio-pages` | 2 |

#### Warning 7 - 3 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 8 - 3 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 9 - 3 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 10 - 3 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |

#### Warning 11 - 3 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |

#### Warning 12 - 3 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 13 - 3 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |

#### Warning 14 - 3 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 15 - 3 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 16 - 2 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-pages` | 1 |

#### Warning 17 - 2 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-pages` | 1 |




---