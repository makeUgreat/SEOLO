package com.c104.seolo.domain.machine.service;

import com.c104.seolo.domain.machine.dto.MachineDto;
import com.c104.seolo.domain.machine.dto.MachineSpaceDto;
import com.c104.seolo.domain.machine.dto.request.MachineRequest;
import com.c104.seolo.domain.machine.dto.response.MachineListResponse;

import java.util.List;

public interface MachineService {
    MachineDto findMachineByMachineId(String companyCode, Long machineId);
    void createMachine(MachineRequest machineRequest, String companyCode);
    void updateMachine(MachineRequest machineRequest, String companyCode, Long machineId);
    void updateMachineSpace(List<MachineSpaceDto> machineSpaceRequest, String companyCode);
    MachineListResponse findMachineByCompanyAndFacility(String companyCode, Long facilityId);
}