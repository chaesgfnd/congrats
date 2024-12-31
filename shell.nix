let
  pkgs =
    import
      #(fetchTarball "https://github.com/NixOS/nixpkgs/archive/cf8cc1201be8bc71b7cbbbdaf349b22f4f99c7ae.tar.gz")
      (fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz")
      { };
	#nixpkgs.url      = "github:NixOS/nixpkgs/nixos-unstable";
in
pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (
      python-pkgs: with python-pkgs; [
        numpy
        telethon
				openai
				requests
      ]
    ))
  ];
}
