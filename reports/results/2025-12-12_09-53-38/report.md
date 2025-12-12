# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-12-12 09:59:34 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 50 |
| **Patched Packages** | 16 |
| **Unpatched Packages** | 34 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 16 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 0 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [invenio-previewer](https://github.com/oarepo/invenio-previewer/tree/contribution-container-previewers) | https://github.com/oarepo/invenio-previewer | contribution-container-previewers |
| [invenio-records-resources](https://github.com/oarepo/invenio-records-resources/tree/contribution-container-extractors) | https://github.com/oarepo/invenio-records-resources | contribution-container-extractors |
| [invenio-rdm-records](https://github.com/oarepo/invenio-rdm-records/tree/contribution-zip-extractors-processors) | https://github.com/oarepo/invenio-rdm-records | contribution-zip-extractors-processors |
| [invenio-app-rdm](https://github.com/oarepo/invenio-app-rdm/tree/contribution-zip-previewer-ui) | https://github.com/oarepo/invenio-app-rdm | contribution-zip-previewer-ui |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-app-rdm` | invenio-previewer invenio-records-resources invenio-rdm-records | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-app-rdm/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-app-rdm/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-app-rdm/test-report-patched.xml)<br>[warnings](packages/invenio-app-rdm/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-previewer` |  | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-previewer/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-previewer/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-previewer/test-report-patched.xml)<br>[warnings](packages/invenio-previewer/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-records-resources` |  | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records-resources/test-report-patched.xml)<br>[warnings](packages/invenio-records-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `invenio-mail` | ⏭️  Skipped |
| `invenio-config` | ⏭️  Skipped |
| `invenio-queues` | ⏭️  Skipped |
| `invenio-oauthclient` | ⏭️  Skipped |
| `invenio-cache` | ⏭️  Skipped |
| `invenio-base` | ⏭️  Skipped |
| `invenio-app` | ⏭️  Skipped |
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
| `invenio-jobs` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-jobs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-jobs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-jobs/test-report-patched.xml)<br>[warnings](packages/invenio-jobs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-drafts-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-drafts-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-drafts-resources/test-report-patched.xml)<br>[warnings](packages/invenio-drafts-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-requests` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-requests/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-requests/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-requests/test-report-patched.xml)<br>[warnings](packages/invenio-requests/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-pages` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pages/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pages/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pages/test-report-patched.xml)<br>[warnings](packages/invenio-pages/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-collections` | invenio-records-resources invenio-rdm-records | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-collections/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-collections/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-collections/test-report-patched.xml)<br>[warnings](packages/invenio-collections/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-checks` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-checks/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-checks/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-checks/test-report-patched.xml)<br>[warnings](packages/invenio-checks/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-audit-logs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-audit-logs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-audit-logs/test-report-patched.xml)<br>[warnings](packages/invenio-audit-logs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-administration` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-administration/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-administration/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-administration/test-report-patched.xml)<br>[warnings](packages/invenio-administration/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-vocabularies` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-vocabularies/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-vocabularies/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-vocabularies/test-report-patched.xml)<br>[warnings](packages/invenio-vocabularies/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-users-resources` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-users-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-users-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-users-resources/test-report-patched.xml)<br>[warnings](packages/invenio-users-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 104 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-requests` | 15 |
| `invenio-app-rdm` | 14 |
| `invenio-users-resources` | 11 |
| `invenio-drafts-resources` | 7 |
| `invenio-jobs` | 7 |
| `invenio-records-resources` | 7 |
| `invenio-vocabularies` | 7 |
| `invenio-audit-logs` | 6 |
| `invenio-banners` | 6 |
| `invenio-collections` | 6 |
| `invenio-github` | 6 |
| `invenio-pages` | 6 |
| `invenio-administration` | 3 |
| `invenio-previewer` | 3 |

#### Warning 2 - 39 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 6 |
| `invenio-vocabularies` | 5 |
| `invenio-jobs` | 4 |
| `invenio-audit-logs` | 3 |
| `invenio-collections` | 3 |
| `invenio-drafts-resources` | 3 |
| `invenio-records-resources` | 3 |
| `invenio-requests` | 3 |
| `invenio-users-resources` | 3 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-pages` | 2 |

#### Warning 3 - 32 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 3 |
| `invenio-collections` | 3 |
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-jobs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-pages` | 2 |
| `invenio-previewer` | 2 |
| `invenio-records-resources` | 2 |
| `invenio-requests` | 2 |
| `invenio-users-resources` | 2 |
| `invenio-vocabularies` | 2 |

#### Warning 4 - 30 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-app-rdm` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-collections` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-jobs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-pages` | 2 |
| `invenio-previewer` | 2 |
| `invenio-records-resources` | 2 |
| `invenio-requests` | 2 |
| `invenio-users-resources` | 2 |
| `invenio-vocabularies` | 2 |

#### Warning 5 - 18 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 6 |
| `invenio-pages` | 6 |
| `invenio-previewer` | 3 |
| `invenio-collections` | 2 |
| `invenio-requests` | 1 |

#### Warning 6 - 16 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 7 - 16 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-collections` | 2 |
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 8 - 15 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 9 - 15 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 10 - 15 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-previewer` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 11 - 15 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 2 |
| `invenio-jobs` | 2 |
| `invenio-vocabularies` | 2 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 12 - 14 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 13 - 13 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 14 - 12 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 15 - 12 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-collections` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 16 - 9 occurrences

ModuleWarning: Module Warning (from ./node_modules/sass-loader/dist/cjs.js):

| Package | Count |
|---------|-------|
| `invenio-previewer` | 9 |

#### Warning 17 - 8 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 2 |
| `invenio-collections` | 2 |
| `invenio-jobs` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 18 - 7 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |
| `invenio-requests` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 19 - 6 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 2 |
| `invenio-collections` | 2 |
| `invenio-previewer` | 2 |

#### Warning 20 - 5 occurrences

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-jobs` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 21 - 5 occurrences

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-users-resources` | 2 |
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 22 - 5 occurrences

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-requests` | 2 |
| `invenio-vocabularies` | 2 |
| `invenio-audit-logs` | 1 |

#### Warning 23 - 4 occurrences

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 24 - 4 occurrences

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 25 - 3 occurrences

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 26 - 3 occurrences

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-collections` | 1 |
| `invenio-previewer` | 1 |

#### Warning 27 - 3 occurrences

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 28 - 3 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-pages` | 1 |
| `invenio-users-resources` | 1 |

#### Warning 29 - 3 occurrences

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-requests` | 1 |
| `invenio-vocabularies` | 1 |

#### Warning 30 - 2 occurrences

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_MAX_FILE_SIZE' is not set. In future, please set it explicitly to define your max file size, or be aware that the default value used i.e. FILES_REST_DEFAULT_MAX_FILE_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-collections` | 1 |

#### Warning 31 - 2 occurrences

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_QUOTA_SIZE' is not set. In future, please set it explicitly to define your quota size, or be aware that the default value used i.e. FILES_REST_DEFAULT_QUOTA_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-collections` | 1 |

#### Warning 32 - 2 occurrences

DeprecationWarning: `es_clear` fixture is deprecated, use `search_clear` instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-requests` | 1 |

#### Warning 33 - 2 occurrences

DeprecationWarning: subject_nested is deprecated. Use subject_combined instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |
| `invenio-collections` | 1 |

#### Warning 34 - 2 occurrences

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 35 - 2 occurrences

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |
| `invenio-records-resources` | 1 |

#### Warning 36 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestAction' because it has a __init__ constructor (from: tests/customizations/test_request_types.py)

| Package | Count |
|---------|-------|
| `invenio-requests` | 1 |

#### Warning 37 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 38 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestReader' because it has a __init__ constructor (from: tests/resources/test_tasks_resources.py)

| Package | Count |
|---------|-------|
| `invenio-vocabularies` | 1 |

#### Warning 39 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 40 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestWriter' because it has a __init__ constructor (from: tests/resources/test_tasks_resources.py)

| Package | Count |
|---------|-------|
| `invenio-vocabularies` | 1 |

#### Warning 41 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('16a55589-6619-4614-833b-ee2f2d16788c'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 42 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('3b688ad0-eb11-4b29-875b-c22a91e8e15d'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 43 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('8f87c7e7-a124-43a2-9b39-f04d80cad173'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 44 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('9d75969c-dc90-40ef-98eb-a9c647ce57b9'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 45 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('b2e196ed-56e1-483f-8fe1-36ab9d0d622d'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 46 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('df2b99c1-b329-426c-a9c2-4ff8197cc239'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 47 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('dfc6870e-d90c-436e-838c-44040c11b8c5'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 48 - 1 occurrence

SAWarning: This declarative base already contains a class with the same class name and module name as invenio_records_resources.factories.factory.MyRecordMetadata, and will be replaced in the string-lookup table.

| Package | Count |
|---------|-------|
| `invenio-records-resources` | 1 |

#### Warning 49 - 1 occurrence

UserWarning: OpenSearch v2 mappings files not found, falling back to Elasticsearch v7 mappings for module mock_module.mappings. Please add the missing OpenSearch os-v2 mappings.

| Package | Count |
|---------|-------|
| `invenio-vocabularies` | 1 |

#### Warning 50 - 1 occurrence

UserWarning: Please specify the OAISERVER_ID_PREFIX configuration.default value is: oai:runnervm6qbrg:

| Package | Count |
|---------|-------|
| `invenio-collections` | 1 |




---