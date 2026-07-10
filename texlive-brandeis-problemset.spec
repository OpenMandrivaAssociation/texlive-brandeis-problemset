%global tl_name brandeis-problemset
%global tl_revision 50991

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.5
Release:	%{tl_revision}.1
Summary:	Document class for COSI Problem sets at Brandeis University (Waltham, MA)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/brandeis-problemset
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-problemset.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/brandeis-problemset.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Brandeis University's computer science ("COSI") courses often assign
"problem sets" which require fairly rigorous formatting. This document
class, which extends article, provides a simple way to typeset these
problem sets in LaTeX. Although the class is compatible with all LaTeX
flavors, XeLaTeX or LuaLaTeX are recommended for fontspec support.

