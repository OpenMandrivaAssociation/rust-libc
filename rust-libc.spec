%bcond_without check
%global debug_package %{nil}

%global crate libc

Name:           rust-%{crate}
Version:        0.2.115
Release:        2
Summary:        Raw FFI bindings to platform libraries like libc

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/libc
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Raw FFI bindings to platform libraries like libc.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       glibc-devel

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+align-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+align-devel %{_description}

This package contains library source intended for building other packages
which use "align" feature of "%{crate}" crate.

%files       -n %{name}+align-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+const-extern-fn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+const-extern-fn-devel %{_description}

This package contains library source intended for building other packages
which use "const-extern-fn" feature of "%{crate}" crate.

%files       -n %{name}+const-extern-fn-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+extra_traits-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extra_traits-devel %{_description}

This package contains library source intended for building other packages
which use "extra_traits" feature of "%{crate}" crate.

%files       -n %{name}+extra_traits-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustc-dep-of-std-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-dep-of-std" feature of "%{crate}" crate.

%files       -n %{name}+rustc-dep-of-std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+rustc-std-workspace-core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustc-std-workspace-core-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-std-workspace-core" feature of "%{crate}" crate.

%files       -n %{name}+rustc-std-workspace-core-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+use_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_std-devel %{_description}

This package contains library source intended for building other packages
which use "use_std" feature of "%{crate}" crate.

%files       -n %{name}+use_std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'glibc-devel'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
