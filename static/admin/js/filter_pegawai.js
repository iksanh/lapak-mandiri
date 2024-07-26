document.addEventListener("DOMContentLoaded", function () {
  const unitKerjaField = document.querySelector("#id_unit_kerja");
  const pegawaiField = document.querySelector("#id_pegawai");

  unitKerjaField.addEventListener("change", function () {
    const unitKerjaId = this.value;
    fetch(`/pegawai/pegawai-by-unit-kerja/?unit_kerja_id=${unitKerjaId}`)
      .then((response) => response.json())
      .then((data) => {
        while (pegawaiField.firstChild) {
          pegawaiField.removeChild(pegawaiField.firstChild);
        }
        data.forEach(function (item) {
          const option = document.createElement("option");
          option.value = item.id;
          option.textContent = item.nama;
          pegawaiField.appendChild(option);
        });
      });
  });
});
