package com.c104.seolo.global.security.entity;

import lombok.extern.slf4j.Slf4j;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.GrantedAuthority;

import java.util.Collection;

@Slf4j
public class DaoCompanycodeToken extends UsernamePasswordAuthenticationToken {

    private String companyCode;

    public DaoCompanycodeToken(Object principal, Object credentials, String companyCode) {
        super(principal, credentials);
        this.companyCode = companyCode;
    }

    public DaoCompanycodeToken(Object principal, Object credentials, Collection<? extends GrantedAuthority> authorities, String companyCode) {
        super(principal, credentials, authorities);
        this.companyCode = companyCode;
    }


    public String getCompanyCode() {
        return companyCode;
    }
}
