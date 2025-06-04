CREATE MIGRATION m16o3dklyrfvvqdgogmtlrsrjcpp33dgjfik7x6ssi5kcl26kzxmfa
    ONTO m1rsnc7cp6pvjbrrzlurvydcmum4ejp6cpbhjxpdd7b3jtgxxpu46a
{
  DROP FUTURE simple_scoping;
  CREATE ABSTRACT TYPE default::Auditable {
      CREATE REQUIRED PROPERTY created_at: std::cal::local_datetime {
          SET default := (std::cal::to_local_datetime(std::datetime_current(), 'Asia/Seoul'));
          SET readonly := true;
      };
  };
  CREATE TYPE default::Meeting EXTENDING default::Auditable {
      CREATE REQUIRED PROPERTY url_code: std::str {
          SET readonly := true;
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
