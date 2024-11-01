%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x22284f69d9eccdf3df7819791c711af193ff8e54
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-tempest
Version:        25.1.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Tempest
License:        ASL 2.0

URL:            https://launchpad.net/puppet-tempest

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet-vcsrepo
Requires:       puppet-openstacklib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Tempest

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n openstack-tempest-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/tempest/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/tempest/



%files
%{_datadir}/openstack-puppet/modules/tempest/


%changelog
* Fri Nov 01 2024 RDO <dev@lists.rdoproject.org> 25.1.0-1
- Update to 25.1.0

* Fri Oct 04 2024 RDO <dev@lists.rdoproject.org> 25.0.0-1
- Update to 25.0.0



