import FWCore.ParameterSet.Config as cms

process = cms.Process( "CREATE" )

process.load( "FWCore.MessageLogger.MessageLogger_cfi" )
process.MessageLogger.cerr.enable = False
process.MessageLogger.cout = cms.untracked.PSet(
  INFO = cms.untracked.PSet(
    reportEvery = cms.untracked.int32( 1 )
  )
)

process.source = cms.Source( "EmptySource"
# , firstRun = cms.untracked.uint32( 1 )
)
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32( 1 )
)

process.AlCaRecoTriggerBitsRcdCreate = cms.EDAnalyzer( "AlCaRecoTriggerBitsRcdUpdate"
, firstRunIOV = cms.uint32( 1 )
, lastRunIOV  = cms.int32( -1 )
, startEmpty  = cms.bool( True )
, listNamesRemove = cms.vstring(
  )
  # parameter sets to define lists of logical expressions
, triggerListsAdd = cms.VPSet(
    cms.PSet(
      listName = cms.string( 'selectGt' )
    , hltPaths = cms.vstring(
        'PhysicsDeclared'
      )
    )
  , cms.PSet(
      listName = cms.string( 'selectL1' )
    , hltPaths = cms.vstring(
        'L1Tech_BPTX_plus_AND_minus.v0'
      , 'L1Tech_BSC_minBias_threshold1.v0 OR L1Tech_BSC_minBias_threshold2.v0'
      , '~L1Tech_BSC_halo_beam2_inner.v0'
      , '~L1Tech_BSC_halo_beam2_outer.v0'
      , '~L1Tech_BSC_halo_beam1_inner.v0'
      , '~L1Tech_BSC_halo_beam1_outer.v0'
      )
    )
  )
)

import CondCore.DBCommon.CondDBSetup_cfi
process.PoolDBOutputService = cms.Service( "PoolDBOutputService"
, CondCore.DBCommon.CondDBSetup_cfi.CondDBSetup
, timetype = cms.untracked.string( 'runnumber' )
, connect  = cms.string( 'sqlite_file:GenericTriggerEventFlag_AlCaRecoTriggerBits.db' )
, toPut    = cms.VPSet(
    cms.PSet(
      record = cms.string( 'AlCaRecoTriggerBitsRcd' )
    , tag    = cms.string( 'AlCaRecoTriggerBits_v0_test' )
    )
  )
)

process.p = cms.Path(
  process.AlCaRecoTriggerBitsRcdCreate
)


