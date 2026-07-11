%global tl_name pictexsum
%global tl_revision 24965

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A summary of PicTeX commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/pictex/summary
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pictexsum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pictexsum.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document summarises the commands of PicTeX. While it is no
substitute for the PicTeX manual itself (available from Personal TeX
inc.), the document is a useful aide-memoire for those who have read the
manual.

