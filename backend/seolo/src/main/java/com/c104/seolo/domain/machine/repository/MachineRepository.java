package com.c104.seolo.domain.machine.repository;

import com.c104.seolo.domain.machine.dto.info.MachineListInfo;
import com.c104.seolo.domain.machine.entity.Machine;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface MachineRepository extends JpaRepository<Machine, Integer> {
    @Query("SELECT new com.c104.seolo.domain.machine.dto.info.MachineListInfo( " +
            "f.id, f.facilityName, " +
            "sc.subcategory, " +
            "m.id, m.name, m.number, m.createdAt, " +
            "CASE WHEN mm.mm_role = 'Main' THEN mm.user.id ELSE null END, " +
            "CASE WHEN mm.mm_role = 'Main' THEN mm.user.employee.employeeName ELSE null END, " +
            "CASE WHEN mm.mm_role = 'Sub' THEN mm.user.id ELSE null END, " +
            "CASE WHEN mm.mm_role = 'Sub' THEN mm.user.employee.employeeName ELSE null END" +
            ") FROM Machine m " +
            "JOIN m.machineSubcategory sc " +
            "JOIN m.facility f " +
            "LEFT JOIN MachineManager mm ON m.id = mm.machine.id " +
            "WHERE f.id = :facilityId AND f.company.companyCode = :companyCode")
    Optional<List<MachineListInfo>> getMachinesByFacilityIdAndCompany(Long facilityId, String companyCode);
}
