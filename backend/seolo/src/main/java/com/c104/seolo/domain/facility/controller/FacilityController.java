package com.c104.seolo.domain.facility.controller;

import com.c104.seolo.domain.facility.dto.request.FacilityRequest;
import com.c104.seolo.domain.facility.dto.response.FacilityBlueprintResponse;
import com.c104.seolo.domain.facility.dto.response.FacilityListResponse;
import com.c104.seolo.domain.facility.service.FacilityService;
import com.c104.seolo.domain.marker.service.MarkerService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.annotation.Secured;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.net.URI;

@RestController
@RequestMapping("facilities")
@RequiredArgsConstructor
@Slf4j
public class FacilityController {
    private final FacilityService facilityService;
    private final MarkerService markerService;

    @Secured("ROLE_MANAGER")
    @GetMapping
    public ResponseEntity<FacilityListResponse> getFacilities(
            @RequestHeader("Company-Code") String companyCode
    ) {
        return ResponseEntity.ok(facilityService.findFacilityByCompany(companyCode));
    }

    @Secured("ROLE_MANAGER")
    @PostMapping
    public ResponseEntity<Void> createFacility(
            @RequestHeader("Company-Code") String companyCode,
            @RequestBody FacilityRequest facilityRequest
    ) {
        facilityService.createFacility(facilityRequest, companyCode);
        URI location = URI.create("/facilities");
        return ResponseEntity.created(location).build();
    }

    @Secured("ROLE_MANAGER")
    @PatchMapping("/{facilityId}")
    public ResponseEntity<Void> updateFacility(
            @RequestHeader("Company-Code") String companyCode,
            @PathVariable("facilityId") Long facilityId,
            @RequestBody FacilityRequest facilityRequest
    ) {
        facilityService.updateFacility(facilityRequest, companyCode, facilityId);
        return ResponseEntity.accepted().build();
    }

    @Secured("ROLE_MANAGER")
    @DeleteMapping("/{facilityId}")
    public ResponseEntity<Void> deleteFacility(
            @RequestHeader("Company-Code") String companyCode,
            @PathVariable("facilityId") Long facilityId
    ) {
        facilityService.deleteFacility(companyCode, facilityId);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/{employeeNum}")
    public FacilityListResponse getFacilitiesOfEmployee(@PathVariable String employeeNum) {
        return facilityService.findFacilitiesByEmployeeNum(employeeNum);
    }

    @Secured("ROLE_MANAGER")
    @PutMapping("/{facilityId}/blueprints")
    public void addBlueprint(@PathVariable Long facilityId, MultipartFile blueprint) {
        facilityService.addBluePrintAtFacility(blueprint,facilityId);
    }

    @Secured("ROLE_MANAGER")
    @GetMapping("/{facilityId}/blueprints")
    public FacilityBlueprintResponse getBlueprint(@PathVariable Long facilityId) {
        return markerService.getBlueprintAndMarkerByFacilityId(facilityId);
    }
}
