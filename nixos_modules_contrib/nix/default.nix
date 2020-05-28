{
  config_exporters = { optionalAttrs, ... }: [ ];
  options = [
    ../../auto-raid0
    ../../auto-luks
  ];
  resources = { ... }: { };
}
