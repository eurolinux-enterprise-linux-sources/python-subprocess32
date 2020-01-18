# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%filter_setup
}

%global srcname subprocess32

Name:           python-subprocess32
Version:        3.2.6
Release:        14%{?dist}
Summary:        Backport of subprocess module from Python 3.2 to Python 2.*

License:        Python
URL:            https://github.com/google/python-subprocess32
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-test

# Fix heap overflow when parsing too many arguments
# upstream fix: https://github.com/google/python-subprocess32/pull/55
Patch0:     fix-heap-overflow.patch

%global _description\
Backport of the subprocess module from Python 3.2 for use on 2.x.\


%description %_description

%package -n python2-subprocess32
Summary: %summary
%{?python_provide:%python_provide python2-subprocess32}

%description -n python2-subprocess32 %_description

%prep
%setup -q -n subprocess32-%{version}

%patch0 -p1


%build
%py2_build


%install
%py2_install


%check
PYTHONPATH=$(pwd) %{__python2} test_subprocess32.py


%files -n python2-subprocess32
%doc README.txt
%license LICENSE
%{python2_sitearch}/_posixsubprocess.so
%{python2_sitearch}/subprocess32*.egg-info
%{python2_sitearch}/subprocess32.py*


%changelog
* Mon Nov 26 2018 Marcel Plch <mplch@redhat.com> - 3.2.6-14
- Backport upstream patch for heap overflow when parsing too many arguments
- Resolves: rhbz#1619386

* Mon May 21 2018 Charalampos Stratakis <cstratak@redhat.com> - 3.2.6-13
- Import into RHEL 7.6 (rhbz#1440695)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2.6-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.6-9
- Python 2 binary package renamed to python2-subprocess32
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.2.6-6
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.6-1
- Update to 3.2.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug  7 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2.5-0.1.rc1
- Update to new upstream release candidate
- Fix build failure on rawhide

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 David Malcolm <dmalcolm@redhat.com> - 3.2.3-1
- initial package

