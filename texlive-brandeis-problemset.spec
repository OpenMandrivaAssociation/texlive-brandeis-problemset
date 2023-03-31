Name:		texlive-brandeis-problemset
Version:	50991
Release:	2
Summary:	Document class for COSI Problem sets at Brandeis University (Waltham, MA)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/brandeis-problemset
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-problemset.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-problemset.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Brandeis University's computer science ("COSI") courses often
assign "problem sets" which require fairly rigorous formatting.
This document class, which extends article, provides a simple
way to typeset these problem sets in LaTeX. Although the class
is compatible with all LaTeX flavors, XeLaTeX or LuaLaTeX are
recommended for fontspec support.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/brandeis-problemset
%doc %{_texmfdistdir}/doc/latex/brandeis-problemset

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
